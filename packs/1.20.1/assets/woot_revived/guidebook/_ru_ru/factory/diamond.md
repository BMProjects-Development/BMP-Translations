---
navigation:
  parent: factory/factory-index.md
  title: "Алмазный"
  icon: "woot_revived:diamond_cell"
  position: 4
---
# Алмазный

Четвертый уровень вашей фабрики.

## Дизайн

Обратите внимание, что фальшивые рассадники, которые выглядят маленькими на превью, не обязательны.

<ItemImage id="layout" scale="0.5"/> [Схема фабрики](../machines-blocks/layout.md#diamond), настроенная на четвертый тир, поможет вам в строительстве.

<GameScene zoom="2.5" interactive={true}>
    <ImportStructure src="../assets/factory/diamond.snbt" />
    <IsometricCamera yaw="195" pitch="6" />
</GameScene>

## Алмазные блоки

<Row>
  <BlockImage id="diamond_pylon" scale="4" p:attached="true" />
  <BlockImage id="diamond_plinth" scale="4" p:attached="true" />
  <BlockImage id="diamond_cell" scale="4" p:attached="true" />
</Row>


Для этого вам понадобятся:
32 <ItemImage id="diamond_pylon" scale="0.5"/> Алмазных пилона,
32 <ItemImage id="diamond_plinth" scale="0.5"/> Алмазных пьедестала,
1 <ItemImage id="diamond_cell" scale="0.5"/> Алмазная ячейка витальности.

<Row>
  <RecipeFor id="diamond_pylon" />
  <RecipeFor id="diamond_plinth" />
  <RecipeFor id="diamond_cell" />
</Row>