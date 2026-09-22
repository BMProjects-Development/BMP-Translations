---
navigation:
  parent: ae2-mechanics/ae2-mechanics-index.md
  title: Сетевые подключения
  icon: fluix_glass_cable
---

# Сетевые подключения

## Что означает термин "сеть"?

Сеть" представляет собой группу [устройств](../ae2-mechanics/devices.md) связанные между собой блоками, которые могут проходить по [каналам](../ae2-mechanics/channels.md),
как [кабели](../items-blocks-machines/cables.md) или полноблочные механизмы и [устройства](../ae2-mechanics/devices.md). 
(<ItemLink id="charger" />, <ItemLink id="interface" />, <ItemLink id="drive" />, и т.д.)
Технически один кабель - это сеть.

Простым способом определения того, что подключено в сети, является использование <ItemLink id="network_tool" />. Он покажет каждый 
компонент сети, по этому если вы видите то, чего не должно быть, или не видите то, что должно быть, значит, у вас проблема.

Например, это 2 отдельные сети.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/2_networks_1.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="1 2 2">
        Сеть 1
  </BoxAnnotation>

<BoxAnnotation color="#915dcd" min="2 0 0" max="3 2 2">
        Сеть 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Это также 2 отдельные сети, поскольку <ItemLink id="quartz_fiber" /> разделяют [энергию](../ae2-mechanics/energy.md)
без сетевого соединения.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/2_networks_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="1 2 2">
        Сеть 1
  </BoxAnnotation>

  <BoxAnnotation color="#915dcd" min="1.3 0 0" max="3 2 2">
        Сеть 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Однако это всего лишь одна сеть, а не две отдельные. [Квантовый мост](../items-blocks-machines/quantum_bridge.md) действует как
беспроводной [плотный кабель](../items-blocks-machines/cables.md#dense-cable), так что оба конца находятся в одной сети.

<GameScene zoom="4" background="transparent">
  <ImportStructure src="../assets/assemblies/actually_1_network.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="7 3 3">
        Вся 1 сеть
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Это также всего лишь 1 сеть, так как увет [кабеля](../items-blocks-machines/cables.md) не имеет никакого отношения к сетевым соединениям, кроме того, что кабели разных цветов не могут
соединяются друг с другом. Все цвета соединяются с изменчивыми (или "бесцветными") кабелями.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/actually_1_network_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="4 2 2">
        Вся 1 сеть
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

## Менее интуитивные соединения
В данном случае это всего лишь 1 сеть, поскольку <ItemLink id="pattern_provider" />, являясь полноблочным устройством, действует как
кабель, а <ItemLink id="inscriber" /> действует аналогично. Таким образом, сетевое соединение проходит через
интерфейс и высекатель.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_network_connection_1.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="4 2 2">
        Вся 1 сеть
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

Чтобы предотвратить это (полезно для многих настроек автокрафта с использованием [подсетей](../ae2-mechanics/subnetworks.md)),
yможно щелкнуть ПКМ по интерфейсу с <ItemLink id="certus_quartz_wrench" /> чтобы сделать его направленным, в этом случае он не будет/
пропускать каналы через одну сторону.

<Row gap="40">
<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_network_connection_2.snbt" />

  <BoxAnnotation color="#915dcd" min="0 0 0" max="2 2 2">
        Сеть 1
  </BoxAnnotation>

  <BoxAnnotation color="#915dcd" min="2 0 0" max="4 2 2">
        Сеть 2
  </BoxAnnotation>

  <IsometricCamera yaw="195" pitch="30" />
</GameScene>

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/pattern_provider_directional_connection.snbt" />

  <BoxAnnotation color="#ee3333" min="1 .3 .3" max="1.3 .7 .7">
        Обратите внимание на то, что кабель не подключается
  </BoxAnnotation>

  <IsometricCamera yaw="255" pitch="30" />
</GameScene>
</Row>

Другими частями, не обеспечивающими направленных сетевых соединений, являются большинство [подчасти](../ae2-mechanics/cable-subparts.md)
[устройства](../ae2-mechanics/devices.md) такие как <ItemLink id="import_bus" />, <ItemLink id="storage_bus" />, и
<ItemLink id="cable_interface" />.

<GameScene zoom="6" background="transparent">
  <ImportStructure src="../assets/assemblies/subpart_no_connection.snbt" />
  <IsometricCamera yaw="195" pitch="30" />
</GameScene>