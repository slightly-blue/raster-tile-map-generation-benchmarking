import './style.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import TileWMS from 'ol/source/TileWMS.js';
import XYZ from 'ol/source/XYZ.js';


const map = new Map({
  target: 'map',
  layers: [
    new TileLayer({
      source: new XYZ({
        url:
          'http://localhost/{z}/{x}/{-y}.jpg',
      }),
    })
  ],
  view: new View({
    center: [0, 0],
    zoom: 2
  })
});
