# LYT · Personal Portfolio / 个人作品集

单文件、无构建、纯静态的双语个人网站，动效由 [GSAP](https://gsap.com)（ScrollTrigger / SplitText / ScrollTo）驱动。

A bilingual, build-free, single-page portfolio powered by GSAP.

## 结构 / Structure

```
personal-site/
├── index.html      # 中文版（默认）/ Chinese (default)
└── en/
    └── index.html  # English version
```

- 英文浏览器首次访问根路径会自动跳到 `/en/`（会话内记住选择）。
- English-browser visitors are redirected to `/en/` on first visit (remembered per session).

## 在线访问 / Live

**https://lyt123422.github.io/portfolio/**

（推送到 `main` 后由 GitHub Pages 自动发布 / Published automatically via GitHub Pages on push to `main`.）

## 修改内容 / Editing

两个文件里所有需要替换的个人信息都用 `✏️` 注释标出：

- 名字与 Logo（`LYT.dev`）
- 一句话介绍、关于我段落
- 统计数字（`data-value`）
- 项目卡片（复制一个 `<article class="project-card">` 即可新增）
- 技能 chips
- 联系邮箱（把 `mailto:hello@example.com` 换成真实邮箱）与社交链接

## 本地预览 / Local preview

```bash
cd personal-site
python -m http.server 8788
# 打开 http://127.0.0.1:8788/
```
