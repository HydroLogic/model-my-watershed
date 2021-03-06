"use strict";

var modificationConfig = require('./modificationConfig.json');

// modKey should be a key in modificationsConfig (eg. 'turf_grass').
function getHumanReadableName(modKey) {
    if (modificationConfig[modKey]) {
        return modificationConfig[modKey].name;
    }
    console.warn('Unknown Land Cover or Conservation Practice: ' + modKey);
    return '';
}

// If no shortName, just use name.
function getHumanReadableShortName(modKey) {
    if (modificationConfig[modKey]) {
        if (modificationConfig[modKey].shortName) {
            return modificationConfig[modKey].shortName;
        } else {
            return modificationConfig[modKey].name;
        }
    }
    console.warn('Unknown Land Cover or Conservation Practice: ' + modKey);
    return '';
}

function getHumanReadableSummary(modKey) {
    if (modificationConfig[modKey]) {
        return modificationConfig[modKey].summary || '';
    }
    console.warn('Unknown Land Cover or Conservation Practice: ' + modKey);
    return '';
}

var getDrawOpts = function(modKey) {
    if (modKey && modificationConfig[modKey] && modificationConfig[modKey].color) {
        return {
            color: modificationConfig[modKey].color,
            opacity: 1,
            weight: 3,
            fillColor: 'url(#fill-' + modKey + ')',
            fillOpacity: 0.74
        };
    } else {
        // Unknown modKey, return generic grey
        return {
            color: '#888',
            opacity: 1,
            weight: 3,
            fillColor: '#888',
            fillOpacity: 0.74
        };
    }
};

module.exports = {
    getHumanReadableName: getHumanReadableName,
    getHumanReadableShortName: getHumanReadableShortName,
    getHumanReadableSummary: getHumanReadableSummary,
    getDrawOpts: getDrawOpts
};
