---
navigation:
    parent: epp_intro/epp_intro-index.md
    title: Шина хранения ME по тегам
    icon: extendedae:tag_storage_bus
categories:
- расширенные устройства
item_ids:
- extendedae:tag_storage_bus
---

# Шина хранения ME по тегам

<GameScene zoom="8" background="transparent">
  <ImportStructure src="../structure/cable_tag_storage_bus.snbt"></ImportStructure>
</GameScene>

Шина хранения ME по тегам — это <ItemLink id="ae2:storage_bus" />, которую можно фильтровать по тегам предметов или жидкостей и которая поддерживает некоторые базовые логические операторы.

Вот несколько примеров:

- Принимать только сырую руду

c:raw_materials/*

- Принимать все слитки и самоцветы

c:ingots/* | c:gems/*
---