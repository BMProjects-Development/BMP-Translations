---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Энергетические ячейки
  icon: energy_cell
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:energy_cell
- ae2:dense_energy_cell
- ae2:creative_energy_cell
---

# Энергетические ячейки

<Row gap="20">
  <BlockImage id="energy_cell" scale="8" p:fullness="4" />

  <BlockImage id="dense_energy_cell" scale="8" p:fullness="4" />

  <BlockImage id="creative_energy_cell" scale="8" />
</Row>

Энергетические ячейки дают сети больше [энергии](../ae2-mechanics/energy.md). Некоторое количество буфера энергии помогает
сгладить скачки потребления энергии при вставке или извлечении большого количества элементов, а большие объемы энергонакопителей
позволяет сети работать, когда энергия не вырабатывается (например, ночью с солнечными батареями), или справляться с огромным мгновенным потреблением энергии
[пространственным хранилищем](../ae2-mechanics/spatial-io.md).

## Заполнение полосок	

<Row>
<BlockImage id="energy_cell" scale="4" p:fullness="0" />
<BlockImage id="energy_cell" scale="4" p:fullness="1" />
<BlockImage id="energy_cell" scale="4" p:fullness="2" />
<BlockImage id="energy_cell" scale="4" p:fullness="3" />
<BlockImage id="energy_cell" scale="4" p:fullness="4" />
</Row>

Полоски на боковой поверхности ячейки соответствуют количеству энергии в ней.

* 0 при заряде менее 25%
* 1 при заряде от 25 до 50 %
* 2 при заряде от 50% до 75%
* 3 при заряде от 75% до 99%
* 4 при заряде выше 99%

## Типы ячеек

* Ячейка <ItemLink id="energy_cell" /> может хранить 200 тыс. АЕ, и для большинства случаев достаточно всего одной, которая легко справляется со скачками напряжения.
    при обычном использовании сети.
* Ячейка <ItemLink id="dense_energy_cell" /> может хранить 1,6 М АЕ и предназначена для тех случаев, когда необходимо обеспечить работу сети за счет накопленной энергии или
    для работы с огромным мгновенным потреблением энергии большими [пространственными хранилищами](../ae2-mechanics/spatial-io.md) установками.
* <ItemLink id="creative_energy_cell" /> - креативный элемент для тестирования, предоставляющий неограниченную мощность или что-то еще.

## Рецепты

<Row>
  <RecipeFor id="energy_cell" />

  <RecipeFor id="dense_energy_cell" />
</Row>
