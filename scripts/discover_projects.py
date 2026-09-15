#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

MANIFEST_PATH = ".research/project.yml"
API = "https://api.github.com"


def request_json(url: str, token: str | None = None):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "jsl-research-registry/1.0"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response), response.headers


def list_public_repositories(owner: str, token: str | None = None) -> list[dict]:
    repos = []
    page = 1
    while True:
        url = f"{API}/users/{urllib.parse.quote(owner)}/repos?per_page=100&page={page}&type=owner&sort=full_name"
        batch, _ = request_json(url, token)
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos


def fetch_manifest(owner: str, repo: str, default_branch: str, token: str | None = None) -> str | None:
    path = urllib.parse.quote(MANIFEST_PATH, safe="/")
    ref = urllib.parse.quote(default_branch)
    url = f"{API}/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(repo)}/contents/{path}?ref={ref}"
    try:
        payload, _ = request_json(url, token)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise
    if payload.get("encoding") != "base64":
        raise RuntimeError(f"Unexpected encoding for {owner}/{repo}:{MANIFEST_PATH}")
    return base64.b64decode(payload["content"]).decode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Discover public JSL project manifests from GitHub.")
    parser.add_argument("--owner", default="LystadJS")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--token-env", default="GITHUB_TOKEN", help="Environment variable containing an optional GitHub token.")
    args = parser.parse_args()
    token = os.getenv(args.token_env)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    found = 0
    try:
        repos = list_public_repositories(args.owner, token)
        for repo in repos:
            manifest = fetch_manifest(args.owner, repo["name"], repo["default_branch"], token)
            if manifest is None:
                continue
            destination = args.output_dir / repo["name"] / ".research" / "project.yml"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(manifest, encoding="utf-8")
            found += 1
            print(f"discovered {args.owner}/{repo['name']}")
    except urllib.error.HTTPError as exc:
        print(f"GitHub API error: HTTP {exc.code}: {exc.reason}", file=sys.stderr)
        return 1

    print(f"Discovered {found} project manifest(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
