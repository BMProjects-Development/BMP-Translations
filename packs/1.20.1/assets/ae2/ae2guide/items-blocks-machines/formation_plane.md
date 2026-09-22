---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Плоскость формирования
  icon: formation_plane
  position: 210
categories:
- devices
item_ids:
- ae2:formation_plane
---

# Плоскость формирования

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../assets/blocks/formation_plane.snbt" />
</GameScene>

Плоскость формирования размещает блоки и сбрасывает предметы. Она работает аналогично <ItemLink id="storage_bus" />,
размещая/сбрасывая предметы, когда они "хранятся" в ней с помощью [устройств](../ae2-mechanics/devices.md), вставляя в [хранилище сети](../ae2-mechanics/import-export-storage.md),
например, <ItemLink id="import_bus" /> и <ItemLink id="interface" />.

<GameScene zoom="6" interactive={true}>
  <ImportStructure src="../assets/assemblies/formation_plane_demonstration.snbt" />
  <IsometricCamera yaw="255" pitch="30" />
</GameScene>

Это [устройство](../ae2-mechanics/devices.md) использует механику, применяемую шинами хранения в таких системах, как [подсети](../example-setups/pipe-subnet.md),
и может заменить собой шины хранения, если вы хотите сбрасывать предметы/размещать блоки вместо транспортировки предметов.

Это [кабельная подчасть](../ae2-mechanics/cable-subparts.md).

## Фильтрация

По умолчанию самолет будет размещать/опускать все, что угодно. Элементы, вставленные в слоты фильтра, будут действовать как белый список,
позволяя размещать только эти конкретные объекты.

Предметы можно перетаскивать в слоты из JEI/REI, даже если у вас на самом деле нет ни одного такого предмета.

## Приоритет

Приоритеты могут быть установлены нажатием на гаечный ключ в правом верхнем углу графического интерфейса.
Поступающие в сеть предметы будут начинаться с хранилища с наивысшим приоритетом.

## Настройки

* Плоскость может быть настроена на размещение блоков в мире или сброс предметов.

## Модернизации

Плоскость формирования поддерживает следующие [улучшения](upgrade_cards.md):

* <ItemLink id="capacity_card" /> увеличивает количество слотов фильтра.
* <ItemLink id="fuzzy_card" /> позволяет плоскости фильтровать по уровню урона и/или игнорировать предметы NBT
* <ItemLink id="inverter_card" /> переключает фильтр с "белого" списка на "черный".

## Рецепт

<RecipeFor id="formation_plane" />
