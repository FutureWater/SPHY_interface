# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SphyPlugin
                                 A QGIS plugin
 Interface for the SPHY model
                             -------------------
        begin                : 2014-09-09
        copyright            : (C) 2014 by W. Terink, FutureWater
        email                : w.terink@futurewater.nl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SphyPlugin class from file SphyPlugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .sphy_plugin import SphyPlugin
    return SphyPlugin(iface)
