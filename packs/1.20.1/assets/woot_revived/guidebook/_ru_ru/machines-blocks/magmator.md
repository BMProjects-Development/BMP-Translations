---
navigation:
  parent: machines-blocks/machines-blocks-index.md
  title: "Магматор"
  icon: "woot_revived:netherite_magmator"
---
# Магматор

<Row>
    <BlockImage id="copper_magmator" scale="2" />
    <BlockImage id="iron_magmator" scale="2" />
    <BlockImage id="gold_magmator" scale="2" />
    <BlockImage id="diamond_magmator" scale="2" />
    <BlockImage id="netherite_magmator" scale="2" />
</Row>

Магматор — это блок для автоматизации <ItemImage id="stygian_anvil" scale="0.5"/> [Стигийской наковальни](anvil.md).

Поместите его под наковальней, и каждые X тиков он будет пытаться создать предмет и положить его в соседний сундук.
Он ничего не будет делать, если рядом с блоком нет ни одного сундука.

Вы также можете кликнуть по блоку с зажатым Shift, чтобы изменить его режим работы с редстоуном.

Вот скорость работы каждого магматора:
- <ItemImage id="copper_magmator" scale="0.5"/> Медный магматор: `<WootConfig key="magmator.copper_tick_rate" />` тиков на крафт
- <ItemImage id="iron_magmator" scale="0.5"/> Железный магматор: `<WootConfig key="magmator.iron_tick_rate" />` тиков на крафт
- <ItemImage id="gold_magmator" scale="0.5"/> Золотой магматор: `<WootConfig key="magmator.gold_tick_rate" />` тиков на крафт
- <ItemImage id="diamond_magmator" scale="0.5"/> Алмазный магматор: `<WootConfig key="magmator.diamond_tick_rate" />` тиков на крафт
- <ItemImage id="netherite_magmator" scale="0.5"/> Незеритовый магматор: `<WootConfig key="magmator.netherite_tick_rate" />` тиков на крафт

## Крафт

<Row>
    <RecipeFor id="copper_magmator" />
    <RecipeFor id="iron_magmator" />
    <RecipeFor id="gold_magmator" />
    <RecipeFor id="diamond_magmator" />
    <RecipeFor id="netherite_magmator" />
</Row>