![Last commit](https://img.shields.io/github/last-commit/DAS-SPB/test_newman?color=9cf\&logo=git)
![GitHub top language](https://img.shields.io/github/languages/top/DAS-SPB/test_newman?color=blue)
![CI](https://github.com/DAS-SPB/test_newman/actions/workflows/ci.yml/badge.svg)

# Newman E2E Testing Demo

An opinionated starter kit that shows how to execute Postman collections with **Newman** both locally and in a GitHub Actions CI pipeline.
It targets a lightweight demo REST API built with **FastAPI** (in-memory DB, token-based auth) and illustrates scalable, data-driven end-to-end scenarios.

---

## Table of Contents

* [Features](#features)
* [Architecture](#architecture)
* [Prerequisites](#prerequisites)
* [Quick Start](#quick-start)
* [Running the Tests](#running-the-tests)
* [Reports](#reports)
* [CI Pipeline](#ci-pipeline)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)

## Features

* **Data-driven testing (DDT)** – one collection, many scenarios: data files live next to requests for easy maintenance.
* **Built-in HTML & JUnit reports** – clear pass/fail summary that can be archived as CI artefacts.
* **One-click GitHub Actions workflow** – runs on `push`, `pull_request`, and manual dispatch.
* **Configurable regression packs** – tag-based execution allows you to target only subsets (`create_user`, `get_user`, etc.).
* **Zero-dependency API stub** – no external services; the minimal FastAPI app starts in seconds.
* **Containerised API** – the FastAPI service can be started with Docker, while tests run on host or in CI.

## Architecture

```text
            +------------------+
            |   Demo FastAPI   |
            |   (Python 3.12)  |
            +---------+--------+
                      |
          Postman Collection + Env
                      |
            +---------v--------+
            |      Newman      |
            |     (Node 20)    |
            +---------+--------+
                      |
                HTML / JUnit
                 Reports
```

## Prerequisites

| Tool                    | Version | Purpose                   |
| ----------------------- | ------- | ------------------------- |
| **Python**              | ≥ 3.11  | demo API                  |
| **Poetry**              | ^1.8    | Python dependency manager |
| **Node.js**             | ≥ 18    | Newman runner             |
| **npm**                 | 9+      | scripts                   |
| *(optional)* **Docker** | ≥ 24    | containerised API         |

> 📦 **Tip**: `nvm` and `pyenv` make switching versions painless.

## Quick Start

```bash
git clone https://github.com/DAS-SPB/test_newman.git
cd test_newman

# 1. Install Python deps & start the API
poetry install
poetry run python app/main.py &

# 2. Install Node deps
npm ci

# 3. Launch the full regression suite
npm run e2e
```

## Running the Tests

### Selective execution

```bash
# Only 'create user' scenarios
npm run e2e:create_user

# Fetch existing user
npm run e2e:get_user
```

## Reports

After each run Newman drops:

* `newman/report.html` – interactive dashboard
* `newman/report.xml` – CI-friendly JUnit

Open the HTML file in a browser or let GitHub Actions expose it as an artefact.

## CI Pipeline

The workflow file lives in `.github/workflows/ci.yml` and performs:

1. Checkout & cache deps
2. Spin up the demo FastAPI service (Docker)
3. Run Newman against the collection on the runner
4. Upload reports & trigger pull-request annotations

Trigger modes:

* **Push** to `master`
* **Pull request** targeting `master`
* **Manual** Run workflow button

## Roadmap

* [ ] Add negative/edge-case scenarios
* [ ] Parallel execution with `newman-reporter-full`
* [ ] Slack/GChat notifications

## Contributing

PRs are welcome! Please open an issue first to discuss what you would like to change.

## License

Distributed under the MIT License. See `LICENSE` for more information.
