# Repository protection checklist

The installed connector can create files and commits but cannot write branch-protection or ruleset settings. Protection remains an owner configuration task; files alone cannot prevent direct pushes.

In repository Settings -> Rules -> Rulesets, protect main: require pull requests, at least one approval, the `UD capture integrity` status check, resolved review conversations, and prohibit force pushes and branch deletion. Limit bypass to the repository owner as needed. Review administrative file changes through CODEOWNERS. No collaborator invitations or access grants were made by this bootstrap.

The CI workflow checks immutable-path changes, event coverage and artifact hashes. These checks become a mandatory merge gate only after the owner enables protection. Keep contributor branches unique and use non-forced, head-checked updates.
