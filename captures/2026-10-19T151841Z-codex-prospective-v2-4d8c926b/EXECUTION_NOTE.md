# Repository-hygiene execution note

Use `PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python replay_complete.py ...` for the documented portable command. Propagating this environment variable to child Python processes prevents the published-policy import from creating untracked bytecode inside its immutable dependency capture.

The first local repository integrity check detected one newly generated Python bytecode cache under the PR213 dependency capture. Only that untracked runtime cache was removed. Published source/witness bytes, numerical code, policies, outputs and archives remain unchanged. A new policy replay with bytecode generation disabled validates this execution setting; the complete raw-and-factor replay already passed. This note is a runtime/packaging clarification, not a new mathematical result or gate revision.
