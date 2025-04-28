# 🕵️‍♂️ Google Dorking Cheatsheet

## What is Google Dorking?

**Google Dorking** (also known as **Google Hacking**) is the practice of using **advanced search operators** in Google (or other search engines) to find **hidden**, **sensitive**, or **interesting** information that regular searches don't easily reveal.

Instead of just typing random keywords, you can give Google precise instructions with operators like `site:`, `filetype:`, `inurl:`, and more.

**Example:**  
Instead of searching for `admin login`, use:
site:example.com inurl:admin

This tells Google: "Find pages inside `example.com` with `admin` in the URL."

---

## 🔥 Why Use Google Dorking?

- To find **hidden login pages** or **admin panels**.
- To discover **open directories** containing files.
- To locate **exposed documents** (PDFs, Word, Excel).
- To search for **configuration files** or **database dumps**.
- Used by **pentesters**, **security researchers**, and (unfortunately) **attackers** too.

> ⚠️ **Important:** Finding public data is legal.  
> Accessing private or restricted content without permission is illegal.

---

## 🎯 Common Google Dorking Operators

| Operator | Purpose | Example |
|:---------|:--------|:--------|
| `site:` | Search within a specific site/domain | `site:example.com` |
| `intitle:` | Find pages with a specific word in the title | `intitle:"login page"` |
| `inurl:` | Find pages with a keyword in the URL | `inurl:admin` |
| `filetype:` | Find files of a specific type | `filetype:pdf site:gov.my` |
| `ext:` | Alternative for `filetype:` | `ext:xls password list` |
| `intext:` | Search for text inside pages | `intext:"confidential document"` |
| `cache:` | Show Google's cached version of a page | `cache:example.com` |
| `related:` | Find related websites | `related:github.com` |
| `allinurl:` | All specified words must appear in the URL | `allinurl:admin login` |
| `allintitle:` | All specified words must appear in the title | `allintitle:login portal` |
| `allintext:` | All specified words must appear in page text | `allintext:username password` |
| `*` (wildcard) | Matches any word(s) | `password * filetype:xls` |
| `OR` | Search for one term OR another | `password OR confidential` |
| `-` | Exclude a word from search | `admin -site:example.com` |

---

## 🔍 Useful Google Dorking Examples

| Target | Dork | Example |
|:-------|:-----|:--------|
| 📁 Directory Listings (Index of) | `intitle:"index of" "parent directory"` | `intitle:"index of" backup` |
| 📄 PDF Files | `filetype:pdf` | `filetype:pdf site:example.com` |
| 🔑 Login Pages | `inurl:login` | `site:example.com inurl:login` |
| 🗂️ Backup Files | `ext:bak OR ext:old OR ext:backup` | `ext:bak database` |
| 🔐 Password Files | `intitle:"index of" password` | `intitle:"index of" passwords.txt` |
| 📧 Email Lists | `filetype:txt intext:@gmail.com` | `filetype:txt intext:@example.com` |
| 📝 Sensitive Documents | `filetype:doc confidential` | `filetype:xls site:example.com "password"` |
| 🎥 Webcam Feeds | `inurl:view.shtml` or `intitle:"webcamXP"` | `intitle:"Live View / - AXIS"` |
| 🔧 Configuration Files | `ext:cfg OR ext:conf OR ext:cnf` | `ext:conf db_password` |

---

## 🛠 Pro Tips

- **Combine operators** for stronger searches:
site:example.com intitle:"index of" backup

- **Use quotes** `"` to search for exact phrases:
"confidential document"

- **Experiment and be creative** — slight wording changes can yield very different results.
- **Don't abuse Google** — if you search too aggressively, Google may block or captcha you. Use incognito or proxies if necessary.

---

# ✨ Quick Reference

| Task | Shortcut Dork |
|:-----|:--------------|
| Search inside a site | `site:example.com` |
| Find login pages | `inurl:login` |
| Find PDFs | `filetype:pdf` |
| Open directories | `intitle:"index of"` |
| Look for database leaks | `filetype:sql password` |

---

# 📚 Extra

You can even search using multiple operators together!

Example: site:edu filetype:pdf intext:"exam results"
(*Finds PDF files about "exam results" on `.edu` sites.*)



