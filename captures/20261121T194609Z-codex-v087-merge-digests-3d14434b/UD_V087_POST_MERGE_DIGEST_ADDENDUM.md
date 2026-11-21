# PB5 v0.87-preview post-merge digest addendum

**Release status.** Candidate only. **Physical Promotion = 0.**

This addendum updates the deployment status in the first v0.87-preview candidate note. PRs #584–#586 are now present on main as two-parent Git merge commits. The earlier review receipts remain GitHub COMMENTED entries, and independent scope-locked approval is still unverified for #583–#586. The release gate remains open and PR #587 remains a draft.

| PR | Merge commit | Git tree | SHA-256 of raw root tree payload |
| --- | --- | --- | --- |
| #584 | fdcafc3841a733fd89716dcaa6c9ba482874ab96 | 88247ebe0dff1c5519e30fc5c571d8b3999e8f0c | a29e4ba47da6ba711ae7f0cbc4bf034f1ffecedbc2c3de85f0ddb16b74b7c1c7 |
| #585 | 57b926540e6284a34fbd550adf5f2c8c2f2b6a8b | 613db86a609b69cdcb3ec3274f4e17d896a04b11 | 0a7df7b883733afd3bd88185f47b3caa8a5be398afd60d4fe7c54b8ec39e2951 |
| #586 | a61e2b2b7bfff2b10be51079d517b1e8e4d347f3 | a7dea504bc784ba9fe1f203f52d03ed0f0eec526 | f0082b85e807c039e2e332ddb6e8c95ee7aa6ee9d17afb574ed8df9a40bf19b8 |

The manifest records both tree digests and their computation. The raw tree digest hashes Git's serialized root tree bytes. The recursive inventory digest hashes the NUL-delimited listing of modes, object IDs and paths. For each PR, the merged capture manifest, its three SHA-256-checked payloads, and its event also agree byte for byte with the pinned PR head and the observed main tip. These checks establish provenance and preserve the mathematical scope recorded in the candidate note. They do not confer independent approval or set a release tag target.
