---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Зарядник
  icon: charger
  position: 310
categories:
- machines
item_ids:
- ae2:charger
---

# Зарядник

<BlockImage id="charger" scale="8" />

Зарядник позволяет заряжать
поддерживаемые инструменты, а также <ItemLink id="certus_quartz_crystal" />.

Питание может осуществляться как сверху, так и снизу, через [кабели](cables.md) AE2 или другие кабели. Он может
принимать энергию AE2 (AE) или Forge Energy (FE). Предметы можно вставлять и вынимать с любой стороны. 
Извлекать можно только результаты, поэтому фильтры, предотвращающие извлечение кристаллов кварца вместо заряженных кристаллов кварца, не нужны. Можно вращать с помощью
<ItemLink id="certus_quartz_wrench" /> для облегчения автоматизации.

Может использоваться для создания <ItemLink id="charged_certus_quartz_crystal" />
из <ItemLink id="certus_quartz_crystal" />, а также <ItemLink id="meteorite_compass" /> из <ItemLink id="minecraft:compass" />.

Чтобы привести его в действие вручную, поместите <ItemLink id="crank" /> сверху или снизу и нажимайте на него ПКМ, пока предмет не зарядится.

Он также служит рабочим местом для деревенского жителя из AE2.

## Простая автоматизация

В качестве примера, вращаемость позволяет полуавтоматизировать зарядные устройства следующим образом:

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/charger_hopper.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Рецепт

<RecipeFor id="charger" />
