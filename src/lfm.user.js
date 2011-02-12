/*
    Banddisam: Band name disambiguation
    Copyright (C) 2011 Ramon Xuriguera

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

// ==UserScript==
// @name           Last FM Track Clustering
// @namespace      http://me.me
// @description    Last.fm track disambiguation
// @include        http://last.fm/music/*
// @include        http://*.last.fm/music
// @include        http://*.last.fm/music/*
// @match          http://*.last.fm/music/*
// @version        0.0.1
// ==/UserScript==

  var obj = document.createElement("script");
  obj.src="http://localhost:8080/injectjs";
  document.getElementsByTagName('body')[0].appendChild(obj);
  console.log(obj);

