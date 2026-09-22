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
- 联系邮箱（当前为 2596851255@qq.com，搜索 `mailto:` 可替换）

## 绑定自定义域名 / Custom domain（待购）

买好域名后按下面三步操作（**顺序不能反**，先配 DNS 再加 CNAME 文件，否则站点会短暂 404）：

1. **买域名**：推荐 Cloudflare Registrar（成本价、无溢价）或 Namesilo / Porkbun；
   国内注册可选阿里云。优先试 `lyt.dev`，被占则考虑 `lyt123422.dev` / `lyt.codes`。
2. **配 DNS**（在域名商的 DNS 面板）：
   - apex（`lyt.dev`）：添加 4 条 A 记录 → `185.199.108.153` `185.199.109.153` `185.199.110.153` `185.199.111.153`
   - www：添加 CNAME 记录 → `lyt123422.github.io`
3. **接 GitHub**：在仓库根目录添加 `CNAME` 文件（内容只有一行，如 `lyt.dev`）并推送；
   然后 GitHub 仓库 Settings → Pages → Custom domain 填入域名，证书签发后勾选 Enforce HTTPS。
4. 最后把 `index.html` / `en/index.html` / `sitemap.xml` / `robots.txt` / 404.html 里的
   `https://lyt123422.github.io/portfolio/` 全局替换成新域名（一次查找替换即可）。

## 本地预览 / Local preview

```bash
cd personal-site
python -m http.server 8788
# 打开 http://127.0.0.1:8788/
```
