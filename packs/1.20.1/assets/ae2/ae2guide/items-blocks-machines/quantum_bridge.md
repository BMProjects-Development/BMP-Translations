---
navigation:
  parent: items-blocks-machines/items-blocks-machines-index.md
  title: Квантовый мост
  icon: quantum_ring
  position: 110
categories:
- network infrastructure
item_ids:
- ae2:quantum_link
- ae2:quantum_ring
---

# Квантовый сетевой мост

![A formed Quantum Network Bridge](../assets/diagrams/quantum_bridge_demonstration.png)

Квантовые сетевые мосты могут протягивать [сети](../ae2-mechanics/me-network-connections.md) на бесконечные расстояния и даже между измерениями.
Они могут передавать в общей сложности 32 канала (независимо от того, как кабели подключены к каждой грани), по существу
действуя, по сути, как беспроводной [плотный кабель](cables.md#dense-cable).

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/quantum_bridge_internal_structure_1.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/quantum_bridge_internal_structure_2.snbt" />

  <BoxAnnotation color="#33dd33" min="1 1 1" max="6 2 3">
        Воображаемый кабель между двумя конечными точками
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Следует отметить, что **обе стороны должны быть загружены в чанк**, поэтому необходимо использовать <ItemLink id="spatial_anchor" /> или другой чанклоадер
если две стороны находятся далеко друг от друга.

# Квантовое кольцо

<BlockImage id="quantum_ring" scale="8" />

Восемь таких блоков, размещенных вокруг <ItemLink id="quantum_link" />, создадут
Квантовый сетевой мост. Только 4 блока <ItemLink id="quantum_ring" />, расположенные рядом с
<ItemLink id="quantum_link" /> будут принимать сетевые соединения,
4 угловых блока не могут подключаться к кабелям.

## Рецепт

<RecipeFor id="quantum_ring" />

# Квантовая камера

<BlockImage id="quantum_link" scale="8" />

Один из таких блоков, окруженный <ItemLink id="quantum_ring" />
создаст квантовый сетевой мост. Этот блок не подключается ни к каким кабелям и регистрируется только
как часть сети только после создания полного моста.

Инвентарь этого блока может содержать только один <ItemLink id="quantum_entangled_singularity" /> и
доступен для автоматизации.

## Рецепт

<RecipeFor id="quantum_link" />
