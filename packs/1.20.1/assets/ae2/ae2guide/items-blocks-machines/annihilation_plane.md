---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Плоскость уничтожения
  icon: annihilation_plane
  position: 210
categories:
- devices
item_ids:
- ae2:annihilation_plane
---

# Плоскость уничтожения

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/blocks/annihilation_plane.snbt" />
</GameScene>

Плоскость уничтожения разрушает блоки и подбирает предметы. Она работает аналогично <ItemLink id="import_bus" />, перемещая предметы
в [хранилище сети](../ae2-mechanics/import-export-storage.md). Для того чтобы предметы были взяты, они должны столкнуться с
лицом плоскости.

Плоскости уничтожения могут быть зачарованы любым зачарованием для кирки, так что да, вы можете наложить на несколько из них безумные уровни удачи и
[автоматической добычи руды](../example-setups/ore-fortuner.md), если ваш модпак позволяет это сделать. Кроме того, шелковое касание
эффективно снижает затраты энергии на разрушение блока, а разрушение дает шанс не тратить энергию.

Это [кабельная подчасть](../ae2-mechanics/cable-subparts.md).

## Фильтрация

Плоскость уничтожения будет разрушать блок или подбирать предмет только в том случае, если она может хранить полученные предметы
в своей сети. Это означает, что для фильтрации одной плоскости, *вы должны ограничить то, что может быть сохранено в ее сети*, скорее всего, поместив ее в
[Подсеть](../ae2-mechanics/subnetworks.md). Шина <ItemLink id="storage_bus" /> или [ячейка](../items-blocks-machines/storage_cells.md)
может быть [разделена](cell_workbench.md) для достижения этой цели.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/annihilation_filtering.snbt" />

  <DiamondAnnotation pos="1 0.5 0.5" color="#00ff00">
        Фильтруется по выпадающим предметам того, что вы хотите разбить.
  </DiamondAnnotation>

  <DiamondAnnotation pos=".5 0.5 2.5" color="#00ff00">
        Разделение на предметы, которые выпадают из того, что вы хотите разбить.
  </DiamondAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Опять же, он фильтрует *по падению предметов*, поэтому, например, если вы хотите отфильтровать разрушение <ItemLink id="minecraft:amethyst_cluster" />,
вам нужна плоскость, зачарованная на шелковое касание, иначе все предыдущие стадии роста ничего не сбросят, и плоскость будет ломать их независимо от этого,
так как сеть всегда может хранить "ничего".

## Recipe

<RecipeFor id="annihilation_plane" />
