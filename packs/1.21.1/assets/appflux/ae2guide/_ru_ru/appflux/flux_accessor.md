---
navigation:
  parent: appflux/appflux-index.md
  title: Аксессор Потока
  icon: appflux:flux_accessor
categories:
- аксессор потока
item_ids:
- appflux:flux_accessor
- appflux:part_flux_accessor
---

# Аксессор Потока

<Row>
<BlockImage id="appflux:flux_accessor" scale="8"></BlockImage>
<GameScene zoom="8" background="transparent">
  <ImportStructure src="../structure/flux_accessor.snbt"></ImportStructure>
</GameScene>
</Row>

Аксессор Потока может вводить/выводить энергию, хранящуюся в вашей ME-сети. По умолчанию у них нет ограничений на ввод/вывод, что можно изменить в конфигурации Appflux.

У них есть быстрый и обычный режимы. В быстром режиме он выводит энергию каждый тик, что может вызвать задержки при интенсивном использовании. В обычном режиме он выводит энергию в зависимости от запасённой энергии цели, что не вызовет проблем с задержками.

* Примечание: Упомянутая здесь "энергия" — это FE, хранящаяся в ваших [Ячейках Хранения FE](./flux_cells.md), а не энергия в [Энергетических Ячейках](ae2:items-blocks-machines/energy_cells.md).
