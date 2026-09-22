---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Шина переключения
  icon: toggle_bus
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:toggle_bus
- ae2:inverted_toggle_bus
---

# Шина переключения

<GameScene zoom="8" background="transparent">
<ImportStructure src="../assets/assemblies/toggle_bus.snbt" />
<IsometricCamera yaw="195" pitch="30" />
</GameScene>

Шина, функционирующая аналогично <ItemLink id="fluix_glass_cable" /> или другим кабелям, но позволяющая переключать состояние соединения с помощью редстоуна.
позволяет переключать состояние соединения с помощью красного камня. Это позволяет отрезать
отрезать участок [МЭ сети](../ae2-mechanics/me-network-connections.md).

При подаче редстоун сигнала деталь включает соединение, <ItemLink id="inverted_toggle_bus" /> обеспечивает обратное поведение, отключая вместо этого соединение.
обратное поведение, отключая соединение.

Следует отметить, что их переключение может привести к перезагрузке сети и пересчету подключенных устройств.

Это [кабельная подчасть](../ae2-mechanics/cable-subparts.md).

## Рецепты

<RecipeFor id="toggle_bus" />

<RecipeFor id="inverted_toggle_bus" />
