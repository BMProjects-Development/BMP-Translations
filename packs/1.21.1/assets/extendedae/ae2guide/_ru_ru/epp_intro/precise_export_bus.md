---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: Шина точного экспорта ME
    icon: extendedae:precise_export_bus
categories:
- расширенные устройства
item_ids:
- extendedae:precise_export_bus
---

# Шина точного экспорта ME

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../structure/cable_precise_export_bus.snbt"></ImportStructure>
</GameScene>

Шина точного экспорта ME экспортирует предметы/жидкости в указанных количествах. Она экспортирует только в том случае, если контейнер может полностью принять весь объем.

## Пример

![Графический интерфейс](../pic/pre_bus_gui1.png)

Это означает экспорт 3 булыжников за операцию. Экспорт прекращается, когда количество булыжников в сети становится меньше 3.

![Графический интерфейс](../pic/pre_bus_gui2.png)

Он также прекращает экспорт, когда целевой контейнер не может вместить все экспортируемое. Сундук теперь может вместить только 2 булыжника, поэтому шина экспорта останавливается.

---
