---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Ячейки хранения
  icon: item_storage_cell_1k
  position: 410
categories:
- tools
item_ids:
- ae2:item_cell_housing
- ae2:fluid_cell_housing
- ae2:cell_component_1k
- ae2:cell_component_4k
- ae2:cell_component_16k
- ae2:cell_component_64k
- ae2:cell_component_256k
- ae2:item_storage_cell_1k
- ae2:item_storage_cell_4k
- ae2:item_storage_cell_16k
- ae2:item_storage_cell_64k
- ae2:item_storage_cell_256k
- ae2:fluid_storage_cell_1k
- ae2:fluid_storage_cell_4k
- ae2:fluid_storage_cell_16k
- ae2:fluid_storage_cell_64k
- ae2:fluid_storage_cell_256k
---

# Storage Cells

<Column>
  <Row>
    <ItemImage id="item_storage_cell_1k" scale="4" />

    <ItemImage id="item_storage_cell_4k" scale="4" />

    <ItemImage id="item_storage_cell_16k" scale="4" />

    <ItemImage id="item_storage_cell_64k" scale="4" />

    <ItemImage id="item_storage_cell_256k" scale="4" />
  </Row>

  <Row>
    <ItemImage id="fluid_storage_cell_1k" scale="4" />

    <ItemImage id="fluid_storage_cell_4k" scale="4" />

    <ItemImage id="fluid_storage_cell_16k" scale="4" />

    <ItemImage id="fluid_storage_cell_64k" scale="4" />

    <ItemImage id="fluid_storage_cell_256k" scale="4" />
  </Row>
</Column>

Ячейки хранения - один из основных методов хранения в Applied Energistics. Они помещаются в <ItemLink id=" drive" />
или <ItemLink id="chest" />.

Объяснение их емкости в байтах и типах приведено в разделе [Байты и Типы](../ae2-mechanics/bytes-and-types.md).

Компоненты хранилища могут быть извлечены из корпуса, если ячейка пуста, щелчком правой кнопки мыши со сдвигом вправо с ячейкой в руке.

## Разделение

Ячейки можно фильтровать, чтобы принимать только определенные элементы, аналогично тому, как можно фильтровать ячейки <ItemLink id="storage_bus" />. Это
осуществляется в ячейке <ItemLink id="cell_workbench" />.

Предметы можно перетаскивать в слоты из JEI/REI, даже если на самом деле у вас нет ни одного такого предмета.

## Улучшения

Ячейки хранения поддерживают следующие [улучшения](upgrade_cards.md), вставляемые через <ItemLink id="cell_workbench" />:

* <ItemLink id="fuzzy_card" /> (недоступно для жидкостных ячеек) позволяет разделить ячейку по уровню урона и/или игнорировать предметы NBT.
* <ItemLink id="inverter_card" /> переключает фильтр с белого списка на черный.
* <ItemLink id="equal_distribution_card" /> выделяет одинаковое количество байт ячейки для каждого типа, так что один тип не может заполнить всю ячейку
* <ItemLink id="void_card" /> аннулирует вставленные элементы, если ячейка заполнена (или выделено место для конкретного типа
    в случае карты равного распределения), что полезно для предотвращения резервирования ферм. Будьте осторожны при разбиении!
* Портативные ячейки могут принимать <ItemLink id="energy_card" />, чтобы увеличить емкость батареи.

## Раскраска

Переносные предметы и ячейки с жидкостью можно окрашивать аналогично кожаной броне, создавая их с помощью красителей.

# Корпуса

Ячейки могут быть выполнены с накопительным компонентом и корпусом или с корпусом вокруг накопительного компонента:

<Row>
  <Recipe id="network/cells/item_storage_cell_1k" />

  <Recipe id="network/cells/item_storage_cell_1k_storage" />
</Row>

Корпуса сами по себе изготавливаются следующим образом:

<Row>
  <RecipeFor id="item_cell_housing" />

  <RecipeFor id="fluid_cell_housing" />
</Row>

# Компоненты системы хранения

Компоненты хранения являются ядром всех ячеек AE2 и определяют их емкость. Каждый уровень увеличивает емкость
в 4 раза и стоит 3 от стоимости предыдущего уровня.

<Column>
  <Row>
    <RecipeFor id="cell_component_1k" />

    <RecipeFor id="cell_component_4k" />

    <RecipeFor id="cell_component_16k" />
  </Row>

  <Row>
    <RecipeFor id="cell_component_64k" />

    <RecipeFor id="cell_component_256k" />
  </Row>
</Column>

# Элементные ячейки

Ячейки для хранения предметов могут вмещать до 63 различных типов предметов и выпускаются во всех стандартных вариантах вместимости.

<Column>
  <Row>
    <Recipe id="network/cells/item_storage_cell_1k_storage" />

    <Recipe id="network/cells/item_storage_cell_4k_storage" />

    <Recipe id="network/cells/item_storage_cell_16k_storage" />
  </Row>

  <Row>
    <Recipe id="network/cells/item_storage_cell_64k_storage" />

    <Recipe id="network/cells/item_storage_cell_256k_storage" />
  </Row>
</Column>

## Переносное хранилище предметов

Они работают как миниатюрные <ItemLink id="chest" /> в кармане или как рюкзак. Их можно заряжать в <ItemLink id="charger" />.

В отличие от стандартных ячеек хранения, их типовая емкость уменьшается по мере увеличения емкости байтов и составляет половину от общей емкости байтов.
общей емкости байтов.

В дополнение к картам модернизации, которые могут получать все ячейки, эти ячейки также принимают <ItemLink id="energy_card" /> для модернизации своих внутренних батарей.

<Column>
  <Row>
    <RecipeFor id="portable_item_cell_1k" />

    <RecipeFor id="portable_item_cell_4k" />

    <RecipeFor id="portable_item_cell_16k" />
  </Row>

  <Row>
    <RecipeFor id="portable_item_cell_64k" />

    <RecipeFor id="portable_item_cell_256k" />
  </Row>
</Column>

# Жидкостные ячейки

Ячейки для хранения жидкостей могут вмещать до 5 различных типов жидкостей и выпускаются во всех стандартных объемах.

<Column>
  <Row>
    <Recipe id="network/cells/fluid_storage_cell_1k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_4k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_16k_storage" />
  </Row>

  <Row>
    <Recipe id="network/cells/fluid_storage_cell_64k_storage" />

    <Recipe id="network/cells/fluid_storage_cell_256k_storage" />
  </Row>
</Column>

## Портативные устройства для хранения жидкостей

Они работают как миниатюрные <ItemLink id="chest" /> в кармане или как рюкзак. Их можно заряжать в <ItemLink id="charger" />.

В отличие от стандартных ячеек памяти, их типовая емкость уменьшается по мере увеличения емкости байтов и составляет половину
общей емкости байтов.

В дополнение к картам модернизации, которые могут получать все ячейки, эти ячейки также принимают карты <ItemLink id="energy_card" /> для модернизации своих внутренних батарей.

<Column>
  <Row>
    <RecipeFor id="portable_fluid_cell_1k" />

    <RecipeFor id="portable_fluid_cell_4k" />

    <RecipeFor id="portable_fluid_cell_16k" />
  </Row>

  <Row>
    <RecipeFor id="portable_fluid_cell_64k" />

    <RecipeFor id="portable_fluid_cell_256k" />
  </Row>
</Column>
