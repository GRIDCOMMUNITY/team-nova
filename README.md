# Civic Issue Tracker

> Report local problems, auto-triage them and track them to resolution.

Hack Day Haldia x GRID community - 6-hour build challenge

**Repo:** `team-nova` | **Stack:** Python / Flask | **Difficulty:** Hard | **Time:** 6 hours

## Brief
Residents report broken roads, water leaks and power cuts. Build a tracker that sorts reports into categories automatically and gives authorities a priority dashboard.

## Core tasks (must-do)
- [ ] Report form (title, description, location, optional photo URL) with validation
- [ ] Auto-categorise into Road / Water / Electricity / Sanitation / Other using keywords or a small model
- [ ] Priority score from urgent keywords, number of similar reports and age
- [ ] Admin dashboard: filter by category and status, sort by priority, counts and a chart
- [ ] Status flow Open -> In Progress -> Resolved, with timestamps and a note on every change
- [ ] Public page: look up an issue by ID and see its timeline
- [ ] Persist everything in SQLite (helper already in app.py)

## Bonus tasks (only after the core works)
- [ ] Map view of reports (Leaflet + OpenStreetMap)
- [ ] Near-duplicate detection using text similarity
- [ ] Notification preview (email / SMS text) when the status changes
- [ ] Classify reports with an open model instead of keywords

## What is already here
- `index.html` - base page that pings `/api/health`
- `app.py` - Flask app with a SQLite helper (`db()`, `init_db()`), `/api/health` and TODO endpoint stubs (they return 501 until you implement them)
- `requirements.txt` - `flask`, `gunicorn`

## Run locally
```bash
pip install -r requirements.txt
python app.py   # then open http://127.0.0.1:5000
```

## Deploy
Any Python host works (for example Render or PythonAnywhere). Start command: `gunicorn app:app`. Free hosts may reset the filesystem on restart, so the SQLite file can reset - fine for a demo.

## Suggested pacing
- Hour 1: read this README, agree on a plan and split the work
- Hours 2-4: build the core tasks
- Hour 5: integrate, polish, then bonus tasks if time allows
- Hour 6: deploy, open the Pull Request, submit on the MLH platform (OrganizerHQ)

## Submission checklist
- [ ] All core tasks work end to end
- [ ] Project is deployed and the live link opens
- [ ] Pull Request created on the Voyage GitHub repository assigned to your team
- [ ] Project submitted on the MLH platform (OrganizerHQ) - instructions are shared at the start of the event

## Rules
- Build new features on top of this starter project and integrate them.
- Teams of 3-4; every member must be present.
- AI tools and open-source / open-weight models are fully allowed.
