**CERBON's Better Beacons** enhances Minecraft's beacon system with a
new user interface, additional features, fresh effects, and new
advancements. This highly configurable mod introduces tertiary effects
(requiring level 5 beacons), expanded payment items including copper
and netherite, and new effects like Long Reach, Phantom Bane, and
Patrol Bane. The mod allows payment items to influence beacon range,
base blocks to affect effect strength, and supports beam redirection
using amethyst clusters and transparency adjustment using tinted glass.

### Configuration

Below are the available options and their defaults. Paths and lists use
the same names as in the mod's config file.

#### Beacon Effects

- `beaconEffects.isTertiaryEffectsEnabled` (default: `true`)
  - Enables tertiary effects for level 5 beacons. When enabled,
    tertiary effects become available in the beacon UI.

- `beaconEffects.levelOneEffects` (default: `["minecraft:speed",
  "minecraft:jump_boost"]`)
  - List of effects available at beacon level 1. These are the
    primary effects that can be selected when the beacon pyramid has
    a single layer.

- `beaconEffects.levelTwoEffects` (default: `["minecraft:haste",
  "better_beacons:long_reach"]`)
  - List of effects available at beacon level 2. These effects
    become available when the beacon pyramid has two layers.

- `beaconEffects.levelThreeEffects` (default: `["minecraft:strength",
  "minecraft:resistance"]`)
  - List of effects available at beacon level 3. These effects
    become available when the beacon pyramid has three layers.

- `beaconEffects.secondaryEffects` (default: `["minecraft:night_vision",
  "minecraft:regeneration", "minecraft:fire_resistance"]`)
  - List of secondary effects that can be selected in addition to
    the primary effect. These effects are available regardless of
    beacon level.

- `beaconEffects.tertiaryEffects` (default: `["better_beacons:phantom_bane",
  "better_beacons:patrol_bane"]`)
  - List of tertiary effects available when the beacon reaches level
    5. These effects require `isTertiaryEffectsEnabled` to be `true`.

#### Beacon Range and Amplifier

- `beaconRangeAndAmplifier.isPaymentItemRangeEnabled` (default: `true`)
  - If `true`, the type of payment item used affects the beacon's
    range. Different payment items provide different range bonuses,
    with copper providing the least range and netherite providing
    the most.

- `beaconRangeAndAmplifier.isBaseBlockAmplifierEnabled` (default: `true`)
  - If `true`, the base block used to construct the beacon pyramid
    affects the strength (amplifier) of primary effects. Stronger
    base blocks like netherite provide stronger effects.

#### Beacon Beam

- `beaconBeam.allowRedirecting` (default: `true`)
  - If `true`, allows the beacon beam to be redirected using
    amethyst clusters. The beam can be redirected horizontally but
    still needs to point to the sky to function.

- `beaconBeam.allowTransparency` (default: `true`)
  - If `true`, allows the beacon beam's opacity to be adjusted
    using tinted glass blocks. Using three tinted glass blocks makes
    the beam invisible.

- `beaconBeam.horizontalMoveLimit` (default: `64`)
  - Maximum horizontal distance the beacon beam can be redirected
    from its original position.

#### Beacon Buttons

- `beaconButtons.cancelButtonRemoveEffects` (default: `true`)
  - If `true`, clicking the cancel button removes all active beacon
    effects from the player.

- `beaconButtons.isCancelButtonTooltipEnabled` (default: `true`)
  - If `true`, displays a tooltip when hovering over the cancel
    button.

- `beaconButtons.isConfirmButtonTooltipEnabled` (default: `true`)
  - If `true`, displays a tooltip when hovering over the confirm
    button.

#### Beacon Payment Items UI

The payment items UI configuration controls which items appear in the
beacon payment interface and their positions. Each payment slot can be
configured with an item and two X positions (one for when tertiary
effects are enabled, one for when they are disabled).

- `beaconPaymentItemsUI.first.item` (default: `"minecraft:netherite_ingot"`)
  - Item ID for the first payment slot.

- `beaconPaymentItemsUI.first.posX` (default: `14`)
  - X position of the first payment slot when tertiary effects are
    disabled.

- `beaconPaymentItemsUI.first.tertiaryPosX` (default: `12`)
  - X position of the first payment slot when tertiary effects are
    enabled.

- `beaconPaymentItemsUI.second.item` (default: `"minecraft:diamond"`)
  - Item ID for the second payment slot.

- `beaconPaymentItemsUI.second.posX` (default: `35`)
  - X position of the second payment slot when tertiary effects are
    disabled.

- `beaconPaymentItemsUI.second.tertiaryPosX` (default: `33`)
  - X position of the second payment slot when tertiary effects are
    enabled.

- `beaconPaymentItemsUI.third.item` (default: `"minecraft:emerald"`)
  - Item ID for the third payment slot.

- `beaconPaymentItemsUI.third.posX` (default: `55`)
  - X position of the third payment slot when tertiary effects are
    disabled.

- `beaconPaymentItemsUI.third.tertiaryPosX` (default: `53`)
  - X position of the third payment slot when tertiary effects are
    enabled.

- `beaconPaymentItemsUI.fourth.item` (default: `"minecraft:gold_ingot"`)
  - Item ID for the fourth payment slot.

- `beaconPaymentItemsUI.fourth.posX` (default: `77`)
  - X position of the fourth payment slot when tertiary effects are
    disabled.

- `beaconPaymentItemsUI.fourth.tertiaryPosX` (default: `75`)
  - X position of the fourth payment slot when tertiary effects are
    enabled.

- `beaconPaymentItemsUI.fifth.item` (default: `"minecraft:iron_ingot"`)
  - Item ID for the fifth payment slot.

- `beaconPaymentItemsUI.fifth.posX` (default: `100`)
  - X position of the fifth payment slot when tertiary effects are
    disabled.

- `beaconPaymentItemsUI.fifth.tertiaryPosX` (default: `97`)
  - X position of the fifth payment slot when tertiary effects are
    enabled.

- `beaconPaymentItemsUI.sixth.item` (default: `"minecraft:copper_ingot"`)
  - Item ID for the sixth payment slot.

- `beaconPaymentItemsUI.sixth.posX` (default: `122`)
  - X position of the sixth payment slot when tertiary effects are
    disabled.

- `beaconPaymentItemsUI.sixth.tertiaryPosX` (default: `119`)
  - X position of the sixth payment slot when tertiary effects are
    enabled.

