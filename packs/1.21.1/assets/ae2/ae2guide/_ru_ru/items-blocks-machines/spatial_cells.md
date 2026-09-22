---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Ячейки хранения пространства
  icon: spatial_storage_cell_128
  position: 410
categories:
- tools
item_ids:
- ae2:spatial_storage_cell_2
- ae2:spatial_storage_cell_16
- ae2:spatial_storage_cell_128
- ae2:spatial_cell_component_2
- ae2:spatial_cell_component_16
- ae2:spatial_cell_component_128
---

# Ячейки хранения пространства

  <Row>
    <ItemImage id="spatial_storage_cell_2" scale="4" />

    <ItemImage id="spatial_storage_cell_16" scale="4" />

    <ItemImage id="spatial_storage_cell_128" scale="4" />
  </Row>

Ячейки хранения пространства могут [хранить физические объёмы пространства](../ae2-mechanics/spatial-io.md). 
Являются частью <ItemLink id="spatial_io_port" />.

В отличии от [ячеек хранения хранилищ](../items-blocks-machines/storage_cells.md), ячейки хранения пространства не могут быть переформатированы.

Повторяю, **ВЫ НЕ МОЖЕТ СБРОСИТЬ, ПЕРЕФОРМАТИРОВАТЬ ИЛИ ИЗМЕНИТЬ РАЗМЕР ЯЧЕЙКИ ХРАНЕНИЯ ПРОСТРАНСТВА, ЕСЛИ ОНА БЫЛА ИСПОЛЬЗОВАНА.** Создайте новую ячейку, если хотите выбрать другой размер. Спасибо за внимание!


## Рецепты

  <Row>
    <Recipe id="network/cells/spatial_storage_cell_2_cubed_storage" />

    <Recipe id="network/cells/spatial_storage_cell_16_cubed_storage" />

    <Recipe id="network/cells/spatial_storage_cell_128_cubed_storage" />
  </Row>

# Корпуса

Ячейки хранения пространства создаются с использованием пространственного компонента:

<Row>
  <Recipe id="network/cells/spatial_storage_cell_2_cubed" />

  <Recipe id="network/cells/spatial_storage_cell_2_cubed_storage" />
</Row>

Сами корпуса создаются так:

  <RecipeFor id="item_cell_housing" />

# Пространственные компоненты

Пространственные компоненты — это основа ячеек хранения пространства. Каждый следующей уровень расширяет объём максимально возможно хранимого пространства в 8 раз.

  <Row>
    <RecipeFor id="spatial_cell_component_2" />

    <RecipeFor id="spatial_cell_component_16" />

    <RecipeFor id="spatial_cell_component_128" />
  </Row>