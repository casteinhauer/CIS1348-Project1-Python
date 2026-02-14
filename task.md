
---
## Task Assignment

```yaml
To: Engineering Intern
From: Senior Engineer
Subject: Apache Server Log Analysis - 404 Referrer Traffic Investigation
```

We've been reviewing our Apache server logs and noticed a significant amount of 404 traffic hitting our servers. This may indicate broken links on external sites pointing to outdated or incorrect URLs on our domain.

To address this issue, we need to analyze which referrers are sending us this 404 traffic and how frequently.

Please provide a script (`analyze_404_referrers.py`) that takes in an apache log and generates a simple tab-delimited table with the following format:
```
referrer	count
http://example.com/page1	125
http://another-site.com/old-link	87
http://third-site.com/broken	45
```

You can find a sample log file in apache_logs.txt.
The output table should include all referrers generating 404 errors, sorted by count in descending order.
**Important:** Some log entries may have a dash (`-`) as the referrer, which indicates direct access (no referrer). These should be **excluded** from your analysis since we're looking for external sites with broken links.

---
## Technical Reference & Specifications

### Apache server log format

For reference, here's what an Apache server log line looks like:

```
192.168.1.100 - - [30/Oct/2025:14:32:10 +0000] "GET /missing-page.html HTTP/1.1" 404 512 "http://external-site.com/page" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
```

The format structure is:
- IP address
- Identity (usually -)
- User (usually -)
- [Timestamp]
- "HTTP Method Path Protocol"
- Status code (we need 404s)
- Size in bytes
- "Referrer URL" (this is what we need)
- "User agent"

**Parsed values from the example above:**

| Field | Value from Example |
|-------|-------------------|
| IP address | 192.168.1.100 |
| Identity | - |
| User | - |
| Timestamp | 30/Oct/2025:14:32:10 +0000 |
| HTTP Method Path Protocol | GET /missing-page.html HTTP/1.1 |
| Status code | **404** |
| Size in bytes | 512 |
| Referrer URL | **http://external-site.com/page** |
| User agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) |

---
### Running the Program

**Important:** The program must be run from the command line with two arguments:

```bash
python analyze_404_referrers.py <log_file> <output_file>
```

- `<log_file>` - the input Apache log file (e.g., apache_logs.txt)
- `<output_file>` - where to save the tab-delimited results (e.g., 404_referrers.txt)

**Example command:**
```bash
python analyze_404_referrers.py apache_logs.txt 404_referrers.txt
```

**Note:** If `python` doesn't work, try `python3` instead.

**Getting Command-Line Arguments in Python:**

Your program needs to access the file names provided by the user. Use the `sys` module to get these:

```python
import sys

log_file = sys.argv[1]      # First argument - input file
output_file = sys.argv[2]   # Second argument - output file
```

- `sys.argv[0]` is always the program name itself
- `sys.argv[1]` is the first argument (the log file)
- `sys.argv[2]` is the second argument (the output file)

---
### Output format

The output file must be tab-delimited (columns separated by a single tab character `\t`, each line ending with `\n`):

```
referrer	count
http://example.com/page1	125
http://another-site.com/old-link	87
http://third-site.com/broken	45
```

---
### Python Usage and Restrictions

**You may use:**
- Dictionaries (basic operations: `dict[key]`, `dict[key] = value`, `for key in dict:`)
- List sort methods (`.sort()`)

**Do not use:**
- Regular expressions (`re` module)
- Exception handling (`try`/`except`/`finally`)
- Lambda expressions
- Functions as arguments (`sorted(key=...)`, `map()`, `filter()`, `reduce()`, etc.)
- Built-in helpers: `any()`, `all()`, `enumerate()`, `zip()`
- Dictionary iteration methods: `.items()`, `.keys()`, `.values()`
- Comprehensions (list/dict/set)
- External libraries: `pandas`, `numpy`, `csv` module
