---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Цветущие блоки истинного кварца
  icon: flawless_budding_quartz
  position: 010
categories:
- misc ingredients blocks
item_ids:
- ae2:flawless_budding_quartz
- ae2:flawed_budding_quartz
- ae2:chipped_budding_quartz
- ae2:damaged_budding_quartz
- ae2:small_quartz_bud
- ae2:medium_quartz_bud
- ae2:large_quartz_bud
- ae2:quartz_cluster
---

# Цветущие блоки истинного кварца

(также см. [Выращивание кварца](../ae2-mechanics/certus-growth.md))

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/budding_blocks.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Бутоны истинного кварца прорастают из цветущих блоков истинного кварца, подобно аметисту. Их можно найти в [метеоритах](../ae2-mechanics/meteorites.md).
Существует 4 уровня цветущих блоков истинного кварца: Безупречный, потресканный, осколочный и поврежденный. Их легче всего определить
с помощью таких модов, как HWYLA, Jade, The One Probe и т.д. (или с помощью экрана f3).

При использовании потресканных, осколочных и поврежденных блоков каждый раз, когда бутон вырастает еще на одну ступень, этот цветущий блок имеет шанс
ухудшиться на один уровень и в конечном итоге превратиться в обычный <ItemLink id="quartz_block" />.

Безупречный цветущий блок не разрушается от растущих бутонов и служит бесконечным источником.

При разрушении обычной киркой они ухудшаются на 1 уровень. Если сломать киркой,
зачарованной на шелковое касание, они не ухудшаться, если только они не были безупречными. **Это означает, что  совершенные зарождающиеся блоки
нельзя поднять и переместить**. Вместо этого можно использовать [пространсвенное хранилище](../ae2-mechanics/spatial-io.md), чтобы забирать и ставить в другом месте совершенные зарождающиеся блоки.

## Рецепты

Потресканные, осколочные и поврежденные блоки можно изготовить, бросив блок предыдущего уровня (или <ItemLink id="quartz_block" />)
в воду с одним или несколькими <ItemLink id="charged_certus_quartz_crystal" />.

Безупречный зарождающийся блок нельзя изготовить, его можно только найти в мире.

<Row>
  <RecipeFor id="damaged_budding_quartz" />

  <RecipeFor id="chipped_budding_quartz" />

  <RecipeFor id="flawed_budding_quartz" />
</Row>
