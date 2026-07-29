#!/usr/bin/env python3
"""
每日更新：MT管理器、Sideloadly、爱思助手、沙漏验机
统一使用 Badge 展示版本号
"""

import re
import json
import requests
import subprocess
import os

README = "README.md"

def get_mt_version():
    url = "https://mt2.cn/download/"
    resp = requests.get(url, timeout=10)
    resp.encoding = 'utf-8'
    match = re.search(r'版本名：([vV]?\d+\.\d+\.\d+)', resp.text)
    if match:
        return match.group(1)
    raise Exception("MT 版本未找到")

def get_sideloadly_version():
    url = "https://sideloadly.io/"
    resp = requests.get(url, timeout=10)
    json_ld = re.search(r'<script type="application/ld\+json">(.*?)</script>', resp.text, re.DOTALL)
    if json_ld:
        data = json.loads(json_ld.group(1))
        if 'softwareVersion' in data:
            return data['softwareVersion']
    match = re.search(r'v(\d+\.\d+\.\d+)', resp.text)
    if match:
        return match.group(1)
    raise Exception("Sideloadly 版本未找到")

def get_aisi_version():
    url = "https://www.i4.cn/pros/pc.html"
    resp = requests.get(url, timeout=10)
    resp.encoding = 'utf-8'
    match = re.search(r'V(\d+\.\d+)', resp.text)
    if match:
        return f"V{match.group(1)}"
    raise Exception("爱思助手版本未找到")

def get_shalou_version():
    url = "https://www.shalou.net/data.json"
    try:
        resp = requests.get(url, timeout=30)
    except requests.exceptions.Timeout:
        raise Exception("沙漏验机连接超时")
    data = resp.json()
    version = data.get("shalouWin64", {}).get("version")
    if version:
        return version
    raise Exception("沙漏验机版本未找到")

def make_badge(version_str):
    ver_match = re.search(r'(\d+\.\d+\.\d+\.?\d*)', version_str)
    if not ver_match:
        ver_match = re.search(r'(\d+\.\d+)', version_str)
    if not ver_match:
        return version_str
    ver = ver_match.group(1)
    is_beta = 'beta' in version_str.lower()
    label = 'beta' if is_beta else 'release'
    color = 'orange' if is_beta else 'blue'
    badge_url = f"https://img.shields.io/badge/{label}-v{ver}-{color}"
    return f"![{label}]({badge_url})"

def update_readme(project_name, new_version):
    with open(README, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    updated = False
    new_lines = []
    badge = make_badge(new_version)

    for line in lines:
        if project_name in line and '|' in line:
            parts = line.split('|')
            if len(parts) >= 5:
                parts[-2] = badge
                new_line = '|'.join(parts)
                if new_line != line:
                    updated = True
                    line = new_line
        new_lines.append(line)

    if updated:
        with open(README, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"✅ 已更新 {project_name} 版本为 {new_version} (Badge)")
        return True
    else:
        print(f"⏭️ {project_name} 版本无变化")
        return False

def daily_update():
    projects = [
        {"name": "MT管理器", "get": get_mt_version},
        {"name": "Sideloadly", "get": get_sideloadly_version},
        {"name": "爱思助手", "get": get_aisi_version},
        {"name": "沙漏验机", "get": get_shalou_version},
    ]

    any_updated = False
    for p in projects:
        try:
            ver = p["get"]()
            if update_readme(p["name"], ver):
                any_updated = True
        except Exception as e:
            print(f"❌ 获取 {p['name']} 版本失败: {e}")

    return any_updated

if __name__ == "__main__":
    if daily_update():
        if os.path.exists('.git'):
            subprocess.run(["git", "config", "user.email", "action@github.com"], check=False)
            subprocess.run(["git", "config", "user.name", "GitHub Action"], check=False)
            subprocess.run(["git", "add", README], check=False)
            subprocess.run(["git", "commit", "-m", "daily: update versions (Badge)"], check=False)
            subprocess.run(["git", "push"], check=False)