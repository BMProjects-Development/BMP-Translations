---
navigation:
  title: Хранилище MEGA
  icon: item_storage_cell_256m
  parent: index.md
  position: 010
categories:
  - megacells
item_ids:
  - cell_component_1m
  - cell_component_4m
  - cell_component_16m
  - cell_component_64m
  - cell_component_256m
  - mega_item_cell_housing
  - mega_fluid_cell_housing
  - mega_chemical_cell_housing
  - mega_source_cell_housing
  - mega_mana_cell_housing
  - mega_experience_cell_housing
  - item_storage_cell_1m
  - item_storage_cell_4m
  - item_storage_cell_16m
  - item_storage_cell_64m
  - item_storage_cell_256m
  - fluid_storage_cell_1m
  - fluid_storage_cell_4m
  - fluid_storage_cell_16m
  - fluid_storage_cell_64m
  - fluid_storage_cell_256m
  - chemical_storage_cell_1m
  - chemical_storage_cell_4m
  - chemical_storage_cell_16m
  - chemical_storage_cell_64m
  - chemical_storage_cell_256m
  - source_storage_cell_1m
  - source_storage_cell_4m
  - source_storage_cell_16m
  - source_storage_cell_64m
  - source_storage_cell_256m
  - mana_storage_cell_1m
  - mana_storage_cell_4m
  - mana_storage_cell_16m
  - mana_storage_cell_64m
  - mana_storage_cell_256m
  - experience_storage_cell_1m
  - experience_storage_cell_4m
  - experience_storage_cell_16m
  - experience_storage_cell_64m
  - experience_storage_cell_256m
  - portable_item_cell_1m
  - portable_item_cell_4m
  - portable_item_cell_16m
  - portable_item_cell_64m
  - portable_item_cell_256m
  - portable_fluid_cell_1m
  - portable_fluid_cell_4m
  - portable_fluid_cell_16m
  - portable_fluid_cell_64m
  - portable_fluid_cell_256m
  - portable_chemical_cell_1m
  - portable_chemical_cell_4m
  - portable_chemical_cell_16m
  - portable_chemical_cell_64m
  - portable_chemical_cell_256m
  - portable_source_cell_1m
  - portable_source_cell_4m
  - portable_source_cell_16m
  - portable_source_cell_64m
  - portable_source_cell_256m
  - portable_mana_cell_1m
  - portable_mana_cell_4m
  - portable_mana_cell_16m
  - portable_mana_cell_64m
  - portable_mana_cell_256m
  - portable_experience_cell_1m
  - portable_experience_cell_4m
  - portable_experience_cell_16m
  - portable_experience_cell_64m
  - portable_experience_cell_256m
  - sky_bronze_ingot
  - sky_bronze_block
  - sky_osmium_ingot
  - sky_osmium_block
---

# MEGA-ячейки: Хранилище

<GameScene zoom="8" background="transparent">
  <ImportStructure src="assets/assemblies/drive_cells.snbt" />
  <IsometricCamera yaw="195" pitch="10" />
</GameScene>

## MEGA [Ячейки хранения](ae2:items-blocks-machines/storage_cells.md)

<Row>
  <ItemImage id="mega_item_cell_housing" scale="4" />
  <ItemImage id="item_storage_cell_1m" scale="4" />
  <ItemImage id="item_storage_cell_4m" scale="4" />
  <ItemImage id="item_storage_cell_16m" scale="4" />
  <ItemImage id="item_storage_cell_64m" scale="4" />
  <ItemImage id="item_storage_cell_256m" scale="4" />
</Row>

Как упоминалось ранее, <ItemLink id="megacells:accumulation_processor" /> служит первым шагом к созданию любой инфраструктуры MEGA, и это включает в себя ее собственные более высокие уровни ячеек хранения для начала. С помощью этого процессора <ItemLink id="ae2:cell_component_256k" /> может быть доведен *еще дальше*, от **1M** (эквивалентно "1024k") до самого высокого уровня M в **256M** — более чем в *тысячу* раз выше по емкости, чем 256k.

<RecipeFor id="cell_component_1m" />
<RecipeFor id="cell_component_4m" />
<RecipeFor id="cell_component_16m" />
<RecipeFor id="cell_component_64m" />
<RecipeFor id="cell_component_256m" />

Конечно, более мощное хранилище потребует более мощного корпуса, и именно здесь в дело вступает еще немного Небесной Стали для создания корпуса ячейки предметов для ваших новых компонентов M-уровня.

<Row>
  <RecipeFor id="mega_item_cell_housing" />
  <Recipe id="cells/standard/item_storage_cell_1m" />
  <Recipe id="cells/standard/item_storage_cell_1m_with_housing" />
</Row>

Для жидкостей и всего остального также существуют специальные корпуса. Как оказалось, Небесный Камень достаточно прочен, чтобы сплавляться с некоторыми другими металлами для образования соответствующих ячеек, например, с медью для изготовления корпусов жидкостных ячеек из **Небесной Бронзы**. Даже за пределами этого руководства, все, что вы можете придумать, может быть поддержано MEGA и специальной ячейкой со своим собственным типом корпуса.

<Row>
  <ItemImage id="sky_bronze_ingot" scale="4" />
  <ItemImage id="mega_fluid_cell_housing" scale="4" />
  <ItemImage id="fluid_storage_cell_1m" scale="4" />
  <ItemImage id="fluid_storage_cell_4m" scale="4" />
  <ItemImage id="fluid_storage_cell_16m" scale="4" />
  <ItemImage id="fluid_storage_cell_64m" scale="4" />
  <ItemImage id="fluid_storage_cell_256m" scale="4" />
</Row>

<Row>
  <Recipe id="transform/sky_bronze_ingot" />
  <RecipeFor id="mega_fluid_cell_housing" />
</Row>

## MEGA [Портативные ячейки](ae2:items-blocks-machines/storage_cells.md#portable-item-storage)

MEGA также предоставляет портативные версии всех своих ячеек, как и сам AE2, хотя увеличенная емкость этих ячеек потребует значительно больше энергии. Таким образом, обратите внимание, что они создаются с помощью <ItemLink id="ae2:dense_energy_cell" /> в отличие от обычной <ItemLink id="ae2:energy_cell" />.

Хотя эти портативные ячейки также поддерживают полный спектр [улучшений](ae2:items-blocks-machines/upgrade_cards.md), которые поддерживают обычные портативные ячейки ME, их увеличенная батарея и общая потребность в энергии означают, что обычная <ItemLink id="ae2:energy_card" /> не *совсем* достаточно сильна, чтобы поддерживать их. Для этой цели подойдет только <ItemLink id="megacells:greater_energy_card" />.

<Row>
  <RecipeFor id="portable_item_cell_1m" />
</Row>