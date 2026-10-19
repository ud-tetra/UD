# Additional explicit schema delta: comparison design

The v0.2 source-specific physical-model schema also tightens `comparison_design` to `RETROSPECTIVE_EXISTING_PUBLIC_ONLY` or null. It removes the old PR250 `FRESH_INDEPENDENT_UNSEEN_SOURCE_REQUIRED` option for this exact, now-exposed candidate. The actual null model request fields remain unchanged. This is a safer source/lane typing restriction, already present in the frozen v0.2 schema before controls ran; this note explicitly records it after a separate review requested clearer disclosure.

This does not forbid fresh confirmation using a genuinely new independently reviewed source and a new source-specific request. It prevents this exact known-exposed path from acquiring a fresh-confirmation label by metadata declaration. No code, schema, freeze, control or original file is modified by this clarification. Physical Promotion=0.
