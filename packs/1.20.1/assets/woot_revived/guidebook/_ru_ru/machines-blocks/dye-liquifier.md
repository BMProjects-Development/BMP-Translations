---
navigation:
  parent: machines-blocks/machines-blocks-index.md
  title: "Растворитель красителей"
  icon: "woot_revived:dye_liquifier"
---
# Растворитель красителей

<BlockImage id="dye_liquifier" scale="5"/>

<ItemImage id="dye_liquifier" scale="0.5"/> Растворитель красителей производит <ItemImage id="pure_dye_fluid_bucket" scale="0.5"/> Чистый краситель, растворяя обычные красители.

Каждый краситель дает разное количество сжиженного цвета. Как только у вас наберется `<WootConfig key="dye_liquifier.color_produce_amount" />` мБ каждого из цветов, механизм немедленно произведет `<WootConfig key="dye_liquifier.pure_dye_produce_amount" />` мБ <ItemImage id="pure_dye_fluid_bucket" scale="0.5"/> Чистого красителя.

Вы можете помещать внутрь как сами красители, так и ингредиенты для них, например, цветы.

<Recipe id="dye_liquifier/white" />

Обратите внимание, что показанный рецепт — это лишь пример работы механизма. Используйте JEI (Just Enough Items) для получения более подробной информации о том, сколько цвета даст каждый отдельный предмет.

## Крафт

<RecipeFor id="dye_liquifier" />