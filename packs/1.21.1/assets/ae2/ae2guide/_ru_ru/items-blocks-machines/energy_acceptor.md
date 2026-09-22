---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Приёмник энергии
  icon: energy_acceptor
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:energy_acceptor
---

# Приёмник энергии

<Row gap="20">
<BlockImage id="energy_acceptor" scale="8" /> 

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/cable_energy_acceptor.snbt" />
</GameScene>
</Row>

Приёмник энергии преобразует обычные формы энергии из других технологических модов во внутреннюю форму [энергии](../ae2-mechanics/energy.md) AE2,
AE. Хотя <ItemLink id="controller" /> также может выполнять эту функцию, лица контроллера очень ценны, поэтому часто лучше использовать вместо него приемник энергии.

Коэффициенты для преобразования FE и E энергии следующие

* 2 FE = 1 AE 
* 1 E = 2 AE

Скорость преобразования полностью зависит от того, сколько АЭ может хранить ваша сеть, по причинам, которые объясняются на
[этой странице](../ae2-mechanics/energy.md).

## Варианты

Приемники энергии выпускаются в двух вариантах: обычном и плоском/[подчасти](../ae2-mechanics/cable-subparts.md). Это позволяет сделать некоторые схемы более компактными.

Приемники энергии можно менять местами между обычными и плоскими в сетке крафта.

## Рецепт

<RecipeFor id="energy_acceptor" />

<RecipeFor id="cable_energy_acceptor" />