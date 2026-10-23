Update the knowledge files of the claude.ai project named "Ask Black Swift Technologies" using Claude in Chrome.

The new files are the `.md` files in EXPORT_DIR whose names do not start with `_`. Never upload `_excluded.md` or anything else starting with `_` or `.`.

Steps:
1. Call tabs_context_mcp, then open a new tab and go to https://claude.ai. Open "Ask Black Swift Technologies": it is pinned in the left sidebar and may not appear on the Projects page. If you can't find it, or the signed-in account isn't the Black Swift Technologies one, stop and report it.
2. In the project knowledge panel, remove each existing file whose name is one of the export file names (for example `projects.md`, `asana_tasks.md`, `proposals_part2.md`), and any `proposals_partN.md` that is no longer in the export. These are earlier copies of files this job uploaded. Do not touch any other file in the project.
3. Upload every export file through the knowledge panel's file input with file_upload. Never click the upload button, because that opens a native picker. Upload them in batches that stay under 10 MB per call.
4. Confirm that every export file name now appears exactly once in the project knowledge list.
5. Close the tab you opened.

Do not change project settings, instructions, sharing or members, and do not start a chat.

Your final line must be exactly `SYNC_OK` on success, or `SYNC_FAILED: <one-line reason>` otherwise.
