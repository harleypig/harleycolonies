**AI Improvements** is a performance optimization mod that reduces CPU
usage from entity AI tasks. It can selectively disable or replace
inefficient AI behaviors for various mob types, including removing look
goals, random movement tasks, and replacing the look controller with a
more efficient cached version. The mod supports per-mob-type
configuration and filter lists for fine-grained control.

### Configuration

Below are the available options and their defaults. Paths and lists use
the same names as in the mod's config file.

#### General

- `allow_remove_calls` (default: `true`)
  - Allows AI tasks to be removed from entities at runtime. If disabled,
    no per-mob or per-mob-type removes will run.

- `enable_call_bubbling` (default: `true`)
  - Allows repeat remove calls to bubble to the top of the list to
    improve performance of repeat mob spawning.

#### Mob AI Tasks

- `remove_look_goal` (default: `false`)
  - Removes the look-at-goal (player or attack target) AI task. This
    causes AIs to not face targets or walking directions.

- `remove_look_random` (default: `false`)
  - Removes the look-at-random-position AI task. This causes AIs to feel
    a little lifeless as they do not animate head movement while idle.

- `replace_look_controller` (default: `true`)
  - Replaces the default look controller with a version featuring cached
    tan math improving performance. Only works on vanilla-style mobs; if
    a mod overrides the look controller it will skip.

Each mob AI task setting includes:

- `is_allowlist` (default: `false`)
  - Set to `true` to apply this setting to all mobs on the filter list.
    Set to `false` to NOT apply this to mobs on the filter list.

- `filter_list` (default: `[]`)
  - List of mobs affected by this setting according to `is_allowlist`.

#### Fish AI Tasks

- `remove_swim` (default: `false`)
  - Removes the fish's random swimming pathfinder. Fish will stay in
    position more often.

- `remove_panic` (default: `false`)
  - Removes the fish's panic pathfinder. Fish will not run away.

- `remove_avoid_player` (default: `false`)
  - Removes the fish's AI task to avoid players.

- `remove_follow_leader` (default: `false`)
  - Removes the fish's AI task to follow a leader fish to act as a group
    of fish.

- `remove_puff` (default: `false`)
  - Removes the fish's AI task to puff up when entities are nearby.

#### Squid AI Tasks

- `remove_flee` (default: `false`)
  - Removes the squid's flee pathfinder. Squid will not run away.

- `remove_random_move` (default: `false`)
  - Removes the squid's random movement pathfinder. Squid will not swim
    around randomly.

#### Cow AI Tasks

- `remove_float` (default: `false`)
  - Removes the cow's float AI task. Cows will no longer swim in water.

- `remove_panic` (default: `false`)
  - Removes the cow's panic AI task. Cows will no longer run around
    after being hit, or search water to extinguish themselves.

- `remove_breed` (default: `false`)
  - Removes the cow's breed AI task. Cows will be unable to breed to
    create offspring.

- `remove_tempt` (default: `false`)
  - Removes the cow's tempt AI task. Cows will no longer follow the
    player if they're holding an item they like.

- `remove_follow_parent` (default: `false`)
  - Removes the cow's follow-parent AI task. Baby cows will no longer
    follow their parents.

- `remove_stroll` (default: `false`)
  - Removes the cow's random stroll AI task. Cows will no longer walk
    around randomly.

#### Chicken AI Tasks

- `remove_float` (default: `false`)
  - Removes the chicken's float AI task. Chickens will no longer swim
    in water.

- `remove_panic` (default: `false`)
  - Removes the chicken's panic AI task. Chickens will no longer run
    around after being hit, or search water to extinguish themselves.

- `remove_breed` (default: `false`)
  - Removes the chicken's breed AI task. Chickens will be unable to
    breed to create offspring.

- `remove_tempt` (default: `false`)
  - Removes the chicken's tempt AI task. Chickens will no longer follow
    the player if they're holding an item they like.

- `remove_follow_parent` (default: `false`)
  - Removes the chicken's follow-parent AI task. Baby chickens will no
    longer follow their parents.

- `remove_stroll` (default: `false`)
  - Removes the chicken's random stroll AI task. Chickens will no longer
    walk around randomly.

#### Pig AI Tasks

- `remove_float` (default: `false`)
  - Removes the pig's float AI task. Pigs will no longer swim in water.

- `remove_panic` (default: `false`)
  - Removes the pig's panic AI task. Pigs will no longer run around
    after being hit, or search water to extinguish themselves.

- `remove_breed` (default: `false`)
  - Removes the pig's breed AI task. Pigs will be unable to breed to
    create offspring.

- `remove_tempt` (default: `false`)
  - Removes the pig's tempt AI task. Pigs will no longer follow the
    player if they're holding an item they like.

- `remove_follow_parent` (default: `false`)
  - Removes the pig's follow-parent AI task. Baby pigs will no longer
    follow their parents.

- `remove_stroll` (default: `false`)
  - Removes the pig's random stroll AI task. Pigs will no longer walk
    around randomly.

#### Sheep AI Tasks

- `remove_float` (default: `false`)
  - Removes the sheep's float AI task. Sheep will no longer swim in
    water.

- `remove_panic` (default: `false`)
  - Removes the sheep's panic AI task. Sheep will no longer run around
    after being hit, or search water to extinguish themselves.

- `remove_breed` (default: `false`)
  - Removes the sheep's breed AI task. Sheep will be unable to breed to
    create offspring.

- `remove_tempt` (default: `false`)
  - Removes the sheep's tempt AI task. Sheep will no longer follow the
    player if they're holding an item they like.

- `remove_follow_parent` (default: `false`)
  - Removes the sheep's follow-parent AI task. Baby sheep will no longer
    follow their parents.

- `remove_stroll` (default: `false`)
  - Removes the sheep's random stroll AI task. Sheep will no longer
    walk around randomly.

- `remove_eat_block` (default: `false`)
  - Removes the sheep's eat-block AI task. Sheep will no longer eat
    grass, and thus be unable to regenerate their wool.

