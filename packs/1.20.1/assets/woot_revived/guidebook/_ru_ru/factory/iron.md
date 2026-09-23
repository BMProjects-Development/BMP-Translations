---
navigation:
  parent: factory/factory-index.md
  title: "Железный"
  icon: "woot_revived:iron_cell"
  position: 2
---
# Железный

Второй уровень вашей фабрики.

## Дизайн

Обратите внимание, что фальшивые рассадники, которые выглядят маленькими на превью, не обязательны.

<ItemImage id="layout" scale="0.5"/> [Схема фабрики](../machines-blocks/layout.md#iron), настроенная на второй тир, поможет вам в строительстве.

<GameScene zoom="2.5" interactive={true}>
    <ImportStructure src="../assets/factory/iron.snbt" />
    <IsometricCamera yaw="195" pitch="6" />
</GameScene>

## Железные блоки

<Row>
  <BlockImage id="iron_pylon" scale="4" p:attached="true" />
  <BlockImage id="iron_plinth" scale="4" p:attached="true" />
  <BlockImage id="iron_cell" scale="4" p:attached="true" />
</Row>

Для этого вам понадобятся:
20 <ItemImage id="iron_pylon" scale="0.5"/> Железных пилонов,
12 <ItemImage id="iron_plinth" scale="0.5"/> Железных пьедесталов,
1 <ItemImage id="iron_cell" scale="0.5"/> Железная ячейка витальности.

<Row>
  <RecipeFor id="iron_pylon" />
  <RecipeFor id="iron_plinth" />
  <RecipeFor id="iron_cell" />
</Row>