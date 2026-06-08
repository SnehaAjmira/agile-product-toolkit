# Agile Product Toolkit

> A comprehensive collection of Agile/Scrum templates, tools, and automation scripts used by Product Owners and Business Analysts to manage the full SDLC — from discovery through UAT and post-go-live stabilization.
>
> ![Agile](https://img.shields.io/badge/Agile-Scrum-009FDA) ![PSPO](https://img.shields.io/badge/PSPO%20I-Certified-green) ![Python](https://img.shields.io/badge/Python-automation-blue?logo=python) ![Jira](https://img.shields.io/badge/Jira-workflow-0052CC?logo=jira)
>
> ---
>
> ## 📌 What's in This Toolkit
>
> This toolkit captures real-world artifacts and automation scripts built while managing products at Eagle Analytical Services and Bright Mind Enrichment. It includes ready-to-use templates aligned with Agile best practices, WSJF prioritization, and regulatory compliance requirements.
>
> ---
>
> ## 📁 Project Structure
>
> ```
> agile-product-toolkit/
> ├── templates/
> │   ├── BRD_template.md              # Business Requirements Document
> │   ├── FRD_template.md              # Functional Requirements Document
> │   ├── user_story_template.md       # User story + acceptance criteria
> │   ├── sprint_planning_template.md  # Sprint planning agenda & checklist
> │   ├── retrospective_template.md    # Sprint retrospective format
> │   └── uat_test_plan_template.md    # UAT test plan template
> ├── scripts/
> │   ├── backlog_prioritizer.py       # WSJF scoring calculator
> │   ├── jira_export_parser.py        # Parse Jira CSV exports to reports
> │   └── sprint_velocity_tracker.py  # Track team velocity over time
> ├── docs/
> │   ├── sdlc_guide.md               # Full SDLC process documentation
> │   └── definitions_of_done.md      # DoD checklist by project phase
> └── README.md
> ```
>
> ---
>
> ## 📋 Templates Included
>
> ### Business Requirements Document (BRD)
> - Executive summary, business objectives, scope
> - - Stakeholder analysis, assumptions, constraints
>   - - High-level requirements and success criteria
>    
>     - ### Functional Requirements Document (FRD)
>     - - System overview and architecture context
>       - - Detailed functional requirements (FR-001 format)
>         - - Non-functional requirements (performance, security, compliance)
>           - - Data flow diagrams and integration points
>            
>             - ### User Story Template
>             - ```
>               As a [role], I want [feature] so that [benefit].
>
>               Acceptance Criteria:
>               - Given [context], when [action], then [outcome]
>               - ...
>
>               Definition of Done:
>               - [ ] Code reviewed
>               - [ ] Unit tests passing
>               - [ ] UAT sign-off obtained
>               - [ ] Documentation updated
>               ```
>
> ### Sprint Planning Checklist
> - [ ] Backlog refined and estimated (WSJF scored)
> - [ ] - [ ] Sprint goal defined and agreed upon
> - [ ] - [ ] Capacity confirmed (accounting for PTO, meetings)
> - [ ] - [ ] Dependencies identified and resolved
> - [ ] - [ ] Definition of Done reviewed
>
> - [ ] ---
>
> - [ ] ## 🔧 Automation Scripts
>
> - [ ] ### `backlog_prioritizer.py` — WSJF Calculator
> - [ ] Implements **Weighted Shortest Job First (WSJF)** scoring to objectively prioritize backlog items by business value, time criticality, risk reduction, and job size.
>
> - [ ] ```bash
> - [ ] python scripts/backlog_prioritizer.py --input backlog.csv --output prioritized_backlog.csv
> - [ ] ```
>
> - [ ] ### `sprint_velocity_tracker.py` — Velocity Dashboard
> - [ ] Tracks sprint velocity over time and generates a trend chart to support sprint planning accuracy.
>
> - [ ] ```bash
> - [ ] python scripts/sprint_velocity_tracker.py --sprints 10
> - [ ] ```
>
> - [ ] ---
>
> - [ ] ## 📊 WSJF Scoring Formula
>
> - [ ] ```
> - [ ] WSJF = Cost of Delay / Job Duration
>
> - [ ] Cost of Delay = Business Value + Time Criticality + Risk Reduction
> - [ ] ```
>
> - [ ] | Story | Business Value | Time Criticality | Risk Reduction | Job Size | WSJF Score |
> - [ ] |---|---|---|---|---|---|
> - [ ] | Feature A | 8 | 5 | 3 | 2 | 8.0 |
> - [ ] | Feature B | 5 | 8 | 2 | 5 | 3.0 |
> - [ ] | Bug Fix C | 3 | 13 | 8 | 1 | 24.0 |
>
> - [ ] ---
>
> - [ ] ## 🚀 Getting Started
>
> - [ ] ```bash
> - [ ] git clone https://github.com/SnehaAjmira/agile-product-toolkit.git
> - [ ] cd agile-product-toolkit
>
> - [ ] # Install Python dependencies for scripts
> - [ ] pip install pandas matplotlib
>
> - [ ] # Run WSJF prioritizer
> - [ ] python scripts/backlog_prioritizer.py --help
> - [ ] ```
>
> - [ ] ---
>
> - [ ] ## 📌 Key Principles
>
> - [ ] - **Always lead with business value** — every user story must connect to a measurable outcome
> - [ ] - **Refine before you sprint** — backlog items should be ready before sprint planning
> - [ ] - **UAT is non-negotiable** — no feature ships without stakeholder sign-off
> - [ ] - **Document as you go** — BRDs and FRDs should be living documents
>
> - [ ] ---
>
> - [ ] *Built by [Sneha Ajmira](https://linkedin.com/in/contactsnehaajmira) | PSPO I Certified Product Owner*
