---
navigation:
  parent: machines-blocks/machines-blocks-index.md
  title: "Наполнитель предметов"
  icon: "woot_revived:item_infuser"
---
# Наполнитель предметов

<BlockImage id="item_infuser" scale="5"/>

<ItemImage id="item_infuser" scale="0.5"/> Наполнитель предметов производит предметы путем объединения ингредиентов и впрыскивания в них жидкости.

## Крафт

<RecipeFor id="item_infuser" />

## Призма

<ItemImage id="prism" scale="0.5"/> Призма — это главный ингредиент для создания <ItemImage id="fake_spawner" scale="0.5"/> Фальшивого рассадника.

<Recipe id="item_infuser/prism" />

## Пластины красителей

Прежде чем получить пластины красителей, вам нужно будет создать специфичный корпус красителя.

Вот пример того, как создать <ItemImage id="white_dye_casing" scale="0.5"/> Корпус белого красителя, но вы можете создать корпус для любого из цветов.

<Row alignItems="center">
  <GameScene zoom="5">
    <ImportStructure src="../assets/anvil/dye_casing.snbt" />
    <IsometricCamera yaw="180" pitch="40" />
  </GameScene>
  <ItemImage id="white_dye_casing" scale="2"/>
  Для его создания вам понадобится <ItemImage id="dye_casing_mold" scale="0.5"/> форма для корпуса красителя и <ItemImage id="minecraft:white_dye" scale="0.5"/> Белый краситель.
</Row>

Как только у вас появится корпус красителя, вы можете использовать его в наполнителе предметов вместе с <ItemImage id="pure_dye_fluid_bucket" scale="0.5"/> Чистым красителем, чтобы получить пластину красителя.

<Recipe id="item_infuser/white_dye_plate" />

## Зачарованные пластины

Для создания ячеек витальности вам понадобятся соответствующие зачарованные пластины.

Например, чтобы получить <ItemImage id="copper_cell" scale="0.5"/> Медную ячейку витальности, вам понадобится <ItemImage id="copper_enchanted_plate" scale="0.5"/> Зачарованная медная пластина.

Для получения этих пластин вам потребуется <ItemImage id="enchanted_fluid_bucket" scale="0.5"/> Зачарованная жидкость, а также соответствующий осколок.

<Row>
  <Recipe id="item_infuser/copper_enchanted_plate" />
  <Recipe id="item_infuser/iron_enchanted_plate" />
  <Recipe id="item_infuser/gold_enchanted_plate" />
  <Recipe id="item_infuser/diamond_enchanted_plate" />
  <Recipe id="item_infuser/netherite_enchanted_plate" />
</Row>

## Разное

Вы также можете получить некоторые ванильные предметы, используя этот механизм.

<Row>
    <Recipe id="item_infuser/magma_block" />
    <Recipe id="item_infuser/netherrack" />
    <Recipe id="item_infuser/fire_charge" />
    <Recipe id="item_infuser/crying_obsidian" />
    <Recipe id="item_infuser/soul_soil" />
</Row>