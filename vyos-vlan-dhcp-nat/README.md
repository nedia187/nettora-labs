# Lab VyOS — VLANs, DHCP & NAT

Laboratoire réseau réalisé sous GNS3 avec un routeur VyOS open source.

## Objectif
Mettre en place une architecture avec 3 VLANs isolés, chacun avec son propre 
serveur DHCP, routés entre eux par VyOS, avec accès Internet via NAT.

## Topologie
- 3 PCs (VPCS) répartis sur VLAN 10, 20, 30
- 1 Switch Ethernet (trunk 802.1Q vers VyOS)
- 1 routeur VyOS 1.5 (routage inter-VLAN, DHCP, NAT)
- 1 nœud NAT1 (simulation accès Internet)

## Compétences mises en pratique
- Déploiement VyOS sous QEMU/GNS3
- VLANs et trunking 802.1Q
- Routage inter-VLAN (sous-interfaces `vif`)
- Serveur DHCP multi-réseaux
- NAT (masquerade)

## Documentation complète
Voir [Lab_VyOS_Simple.pdf](./Lab_VyOS_Simple.pdf) pour la topologie illustrée 
et la configuration CLI complète.

---
Projet **Nettora** — Network Security & Automation Lab
