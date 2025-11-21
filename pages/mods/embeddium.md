---
title: Embeddium
---



Client/Server: client

**Embeddium** is a performance-focused rendering mod for Minecraft that
provides various rendering optimizations and quality settings. The mod
includes chunk building optimizations, entity culling, fog occlusion, and
various rendering performance improvements. It also provides configurable
quality settings for weather, leaves, and other visual effects.

### Configuration

Below are the available options and their defaults. Paths and values use
the same names as in the mod's config file, `embeddium-options.json`.

#### Quality Settings

- `quality.weather_quality` (default: `"DEFAULT"`)
  - Quality setting for weather rendering. Controls the detail level of
    weather effects.

- `quality.leaves_quality` (default: `"DEFAULT"`)
  - Quality setting for leaves rendering. Controls the detail level of
    leaf rendering.

- `quality.enable_vignette` (default: `true`)
  - Enable vignette effect. When enabled, adds a subtle darkening effect
    around the edges of the screen.

- `quality.use_quad_normals_for_shading` (default: `false`)
  - Use quad normals for shading calculations. When enabled, uses more
    accurate shading but may impact performance.

#### Advanced Settings

- `advanced.enable_memory_tracing` (default: `false`)
  - Enable memory tracing. When enabled, tracks memory usage for
    debugging purposes.

- `advanced.use_advanced_staging_buffers` (default: `true`)
  - Use advanced staging buffers for rendering. When enabled, improves
    rendering performance.

- `advanced.disable_incompatible_mod_warnings` (default: `false`)
  - Disable warnings for incompatible mods. When enabled, suppresses
    compatibility warnings.

- `advanced.cpu_render_ahead_limit` (default: `3`)
  - CPU render ahead limit. Controls how many frames ahead the CPU can
    prepare for rendering.

#### Performance Settings

- `performance.chunk_builder_threads` (default: `0`)
  - Number of threads to use for chunk building. `0` means automatic
    detection. Higher values can improve chunk loading performance but use
    more CPU resources.

- `performance.always_defer_chunk_updates_v2` (default: `true`)
  - Always defer chunk updates. When enabled, chunk updates are deferred
    to improve performance.

- `performance.animate_only_visible_textures` (default: `true`)
  - Animate only visible textures. When enabled, texture animations are
    skipped for non-visible textures, improving performance.

- `performance.use_entity_culling` (default: `true`)
  - Use entity culling. When enabled, entities outside the view frustum
    are not rendered.

- `performance.use_fog_occlusion` (default: `true`)
  - Use fog occlusion. When enabled, objects hidden by fog are not
    rendered.

- `performance.use_block_face_culling` (default: `true`)
  - Use block face culling. When enabled, hidden block faces are not
    rendered.

- `performance.use_compact_vertex_format` (default: `true`)
  - Use compact vertex format. When enabled, uses a more memory-efficient
    vertex format.

- `performance.use_translucent_face_sorting_v2` (default: `true`)
  - Use translucent face sorting. When enabled, improves rendering of
    translucent blocks.

- `performance.use_render_pass_optimization` (default: `true`)
  - Use render pass optimization. When enabled, optimizes rendering passes
    for better performance.

- `performance.use_no_error_g_l_context` (default: `true`)
  - Use no-error GL context. When enabled, disables OpenGL error checking
    for better performance (use with caution).

#### Notification Settings

- `notifications.has_cleared_donation_button` (default: `false`)
  - Whether the donation button has been cleared. Used internally.

- `notifications.has_seen_donation_prompt` (default: `false`)
  - Whether the donation prompt has been seen. Used internally.

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

### Modpacks

This mod is installed in the following modpacks:

- harleycolonies-1.21.1

