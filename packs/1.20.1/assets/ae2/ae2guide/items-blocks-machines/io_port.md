---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: МЭ порт ввода/вывода
  icon: io_port
  position: 210
categories:
- devices
item_ids:
- ae2:io_port
---

# МЭ порт ввода/вывода

<BlockImage id="io_port" p:powered="true" scale="8" />

Порт ввода-вывода позволяет быстро заполнять или опустошать [ячейки хранения](../items-blocks-machines/storage_cells.md) в или из
[хранилища сети](../ae2-mechanics/import-export-storage.md).

Его можно вращать с помощью <ItemLink id="certus_quartz_wrench" />.

## Настройки

* Порт ввода-вывода может быть настроен на перемещение ячейки к выходным слотам, когда ячейка пуста, заполнена или когда работа закончена.
* Если вставить <ItemLink id="redstone_card" />, то появятся опции для различных состояний красного камня.
* В центре графического интерфейса находится стрелка, с помощью которой можно выбрать направление передачи предметов: из ячейки в [хранилище сети](../ae2-mechanics/import-export-storage.md),
    или из хранилища в ячейку.

## Модернизации

Порт ввода-вывода поддерживает следующие [улучшения](upgrade_cards.md):

* <ItemLink id="speed_card" /> увеличивает количество перемещаемого материала за одну операцию.
* <ItemLink id="redstone_card" /> добавляет управление красным камнем, позволяя активировать его по высокому, низкому сигналу или один раз за импульс.

## Рецепт

<RecipeFor id="io_port" />
