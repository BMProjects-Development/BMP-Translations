---
navigation:
    parent: machines-blocks/machines-blocks-index.md
    title: "Magmator"
    icon: "woot_revived:netherite_magmator"
---
# Magmator

<Row>
    <BlockImage id="copper_magmator" scale="2" />
    <BlockImage id="iron_magmator" scale="2" />
    <BlockImage id="gold_magmator" scale="2" />
    <BlockImage id="diamond_magmator" scale="2" />
    <BlockImage id="netherite_magmator" scale="2" />
</Row>

The Magmator is the automation block for the <ItemImage id="stygian_anvil" scale="0.5"/> [Stygian Anvil](anvil.md).

Place it underneath the anvil and each X ticks, it will try to craft the item and place it inside a neighbor chest.
It will don't do anything if no chest are available at the side of the block.

You can also shift click the block to change the redstone mode of it.

Here is the tick rate of each magmator:
- <ItemImage id="copper_magmator" scale="0.5"/> Copper Magmator: <WootConfig key="magmator.copper_tick_rate" /> ticks/craft
- <ItemImage id="iron_magmator" scale="0.5"/> Iron Magmator: <WootConfig key="magmator.iron_tick_rate" /> ticks/craft
- <ItemImage id="gold_magmator" scale="0.5"/> Gold Magmator: <WootConfig key="magmator.gold_tick_rate" /> ticks/craft
- <ItemImage id="diamond_magmator" scale="0.5"/> Diamond Magmator: <WootConfig key="magmator.diamond_tick_rate" /> ticks/craft
- <ItemImage id="netherite_magmator" scale="0.5"/> Netherite Magmator: <WootConfig key="magmator.netherite_tick_rate" /> ticks/craft

## Craft

<Row>
    <RecipeFor id="copper_magmator" />
    <RecipeFor id="iron_magmator" />
    <RecipeFor id="gold_magmator" />
    <RecipeFor id="diamond_magmator" />
    <RecipeFor id="netherite_magmator" />
</Row>