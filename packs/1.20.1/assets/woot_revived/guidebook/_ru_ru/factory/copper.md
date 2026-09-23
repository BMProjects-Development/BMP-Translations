---
navigation:
  parent: factory/factory-index.md
  title: "Медный"
  icon: "woot_revived:copper_cell"
  position: 1
---
# Медный

Первый тир вашей фабрики, это её минимальная версия.

Идеально подходит для начала работы с модом или для постройки базовой фабрики на одного моба!

## Дизайн

Сначала вам нужно будет построить центральную базу фабрики, а затем вы сможете завершить окружение.

<ItemImage id="layout" scale="0.5"/> [Схема фабрики](../machines-blocks/layout.md#copper), настроенная на первый тир, поможет вам в строительстве.

<Row>
    <GameScene zoom="2.5" interactive={true}>
        <ImportStructure src="../assets/factory/copper_half.snbt" />
        <IsometricCamera yaw="195" pitch="6" />
    </GameScene>

    <GameScene zoom="2.5" interactive={true}>
        <ImportStructure src="../assets/factory/copper.snbt" />
        <IsometricCamera yaw="195" pitch="6" />
    </GameScene>
</Row>

## Медные блоки

<Row>
  <BlockImage id="copper_pylon" scale="4" p:attached="true" />
  <BlockImage id="copper_plinth" scale="4" p:attached="true" />
  <BlockImage id="copper_cell" scale="4" p:attached="true" />
</Row>

Для фабрики вам понадобятся блоки из раздела [Общие блоки](common-blocks.md), а также несколько блоков, специфичных для данного тира.

Для этого вам понадобятся:
17 <ItemImage id="copper_pylon" scale="0.5"/> Медных пилонов,
6 <ItemImage id="copper_plinth" scale="0.5"/> Медных пьедесталов,
1 <ItemImage id="copper_cell" scale="0.5"/> Медная ячейка витальности.

<Row>
  <RecipeFor id="copper_pylon" />
  <RecipeFor id="copper_plinth" />
  <RecipeFor id="copper_cell" />
</Row>