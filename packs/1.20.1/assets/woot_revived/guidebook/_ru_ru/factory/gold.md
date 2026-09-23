---
navigation:
  parent: factory/factory-index.md
  title: "Золотой"
  icon: "woot_revived:gold_cell"
  position: 3
---
# Золотой

Третий уровень вашей фабрики.

## Дизайн

Обратите внимание, что фальшивые рассадники, которые выглядят маленькими на превью, не обязательны.

<ItemImage id="layout" scale="0.5"/> [Схема фабрики](../machines-blocks/layout.md#gold), настроенная на третий тир, поможет вам в строительстве.

<GameScene zoom="2.5" interactive={true}>
    <ImportStructure src="../assets/factory/gold.snbt" />
    <IsometricCamera yaw="195" pitch="6" />
</GameScene>

## Золотые блоки

<Row>
  <BlockImage id="gold_pylon" scale="4" p:attached="true" />
  <BlockImage id="gold_plinth" scale="4" p:attached="true" />
  <BlockImage id="gold_cell" scale="4" p:attached="true" />
</Row>


Для этого вам понадобятся:
36 <ItemImage id="gold_pylon" scale="0.5"/> Золотых пилонов,
24 <ItemImage id="gold_plinth" scale="0.5"/> Золотых пьедесталов,
1 <ItemImage id="gold_cell" scale="0.5"/> Золотая ячейка витальности.

<Row>
  <RecipeFor id="gold_pylon" />
  <RecipeFor id="gold_plinth" />
  <RecipeFor id="gold_cell" />
</Row>