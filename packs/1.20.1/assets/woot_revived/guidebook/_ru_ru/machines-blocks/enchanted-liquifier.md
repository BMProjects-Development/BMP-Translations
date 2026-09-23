---
navigation:
  parent: machines-blocks/machines-blocks-index.md
  title: "Растворитель чар"
  icon: "woot_revived:enchanted_liquifier"
---
# Растворитель чар

<BlockImage id="enchanted_liquifier" scale="5"/>

<ItemImage id="enchanted_liquifier" scale="0.5"/> Растворитель чар производит <ItemImage id="enchanted_fluid_bucket" scale="0.5"/> Зачарованную жидкость, растворяя зачарованные книги.

Каждый уровень зачарования в книге будет давать `<WootConfig key="enchanted_liquifier.per_enchant_fluid" />` мБ <ItemImage id="enchanted_fluid_bucket" scale="0.5"/> Зачарованной жидкости. Максимум до `<WootConfig key="enchanted_liquifier.max_enchant_lvl" />` уровней.

Это означает, что если в книге есть чары с уровнем выше `<WootConfig key="enchanted_liquifier.max_enchant_lvl" />`, они будут расцениваться механизмом как чары `<WootConfig key="enchanted_liquifier.max_enchant_lvl" />`-го уровня.

<EnchantedRecipe />

## Крафт

<RecipeFor id="enchanted_liquifier" />