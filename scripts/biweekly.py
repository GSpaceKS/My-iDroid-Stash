"""
每半月更新：Scene、unc0ver、checkra1n、iMazing
统一使用 Badge 展示版本号
"""

import re
import os
import datetime
import requests
import subprocess
import sys

README = "README.md"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

TOOL_COL_INDEX = 2          # split('|') 后，工具名称所在的列表索引（0 为首位空字符串，2 对应第3列）
VERSION_COL_INDEX = 5       # split('|') 后，版本号所在的列表索引（5 对应第6列）
MIN_COLS = 7                # split('|') 后列表所需的最小元素数（6列数据 + 1个前导空字符串）

today_day = datetime.datetime.today().day
if today_day not in [1, 16]:
    print(f"今天是 {today_day} 号，不是 1 号或 16 号，跳过。")
    sys.exit(0)


def get_scene_version():
    url = "https://vtools.oss-cn-beijing.aliyuncs.com/vi/Scene9.json"
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.encoding = 'utf-8'
    data = resp.json()
    version = data.get("versionName")
    if version:
        return version
    raise Exception("Scene 版本未找到")


def get_unc0ver_version():
    url = "https://unc0ver.dev/"
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.encoding = 'utf-8'
    match = re.search(r'v(\d+\.\d+\.\d+)', resp.text)
    if match:
        return f"v{match.group(1)}"
    raise Exception("unc0ver 版本未找到")


def get_checkra1n_version():
    url = "https://checkra.in/releases/"
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.encoding = 'utf-8'
    text = resp.text
    match = re.search(r'checkra1n\s+(\d+\.\d+\.\d+)\s+beta', text)
    if match:
        return f"{match.group(1)} beta"
    match = re.search(r'checkra1n\s+(\d+\.\d+\.\d+)', text)
    if match:
        return match.group(1)
    raise Exception("checkra1n 版本未找到")


def get_imazing_version():
    url = "https://imazing.com/download"
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.encoding = 'utf-8'
    text = resp.text
    match = re.search(r'Version:</p>\s*<p><b>([\d.]+)</b></p>', text, re.DOTALL)
    if match:
        return match.group(1)
    match = re.search(r'Version:\s*([\d.]+)', text, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r'<p><b>([\d.]+)</b></p>', text)
    if match:
        return match.group(1)
    raise Exception("iMazing 版本未找到")


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
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|') and stripped.count('|') >= MIN_COLS - 1:
            parts = line.split('|')
            if len(parts) >= MIN_COLS:
                tool = parts[TOOL_COL_INDEX].strip()
                if tool == project_name:
                    old_badge = parts[VERSION_COL_INDEX].strip()  # 获取当前 Badge
                    if old_badge != badge:
                        parts[VERSION_COL_INDEX] = badge
                        line = '|'.join(parts)
                        updated = True
                        print(f"✅ 已更新 {project_name} 版本为 {new_version} (Badge)")
                    else:
                        print(f"⏭️ {project_name} 版本无变化")
        new_lines.append(line)

    if updated:
        with open(README, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    else:
        return False


def biweekly_update():
    projects = [
        {"name": "Scene", "get": get_scene_version},
        {"name": "unc0ver", "get": get_unc0ver_version},
        {"name": "checkra1n", "get": get_checkra1n_version},
        {"name": "iMazing", "get": get_imazing_version},
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
    if biweekly_update():
        if os.path.exists('.git'):
            subprocess.run(["git", "config", "user.email", "action@github.com"], check=False)
            subprocess.run(["git", "config", "user.name", "GitHub Action"], check=False)
            subprocess.run(["git", "add", README], check=False)
            subprocess.run(["git", "commit", "-m", "biweekly: update versions (Badge)"], check=False)
            subprocess.run(["git", "push"], check=False)
        else:
            print("⚠️ 不在 git 仓库中，跳过提交")
