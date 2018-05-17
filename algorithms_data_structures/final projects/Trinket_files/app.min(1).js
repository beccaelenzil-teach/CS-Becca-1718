(function (hljs) {
  // save the original implementations of code, image and link handling
  // from the marked library so we can defer to them in cases
  // where our custom features are not relevant
  var originalCode = marked.Renderer.prototype.code;
  var originalImage = marked.Renderer.prototype.image;
  var originalLink = marked.Renderer.prototype.link;
  var trinket_hosts = trinketConfig.get('apphostname') === 'trinket.io' ? ['trinket.io'] : [
      trinketConfig.get('apphostname'),
      'trinket.io'
    ];
  var trinket_types = [
      'console',
      'python',
      'turtle',
      'charts',
      'processing',
      'html',
      'music',
      'glowscript',
      'blocks',
      'python3',
      'java',
      'glowscript-blocks',
      'R'
    ];
  var python_types = [
      'turtle',
      'charts',
      'processing'
    ];
  var inline_trinkets = [
      'python',
      'python3',
      'html',
      'glowscript',
      'java',
      'R'
    ];
  var EMBED_URLS = [
      {
        regex: /^(?:https?\:)?\/\/(?:www\.)?youtu\.?be(?:\.com)?\/(?:watch\?v=|embed\/)?(\S+)$/i,
        attrs: 'width="420" height="315" frameborder="0" allowfullscreen',
        url: function (match) {
          return '//www.youtube.com/embed/' + match[1];
        }
      },
      {
        regex: /^(?:https?\:)?\/\/(?:www\.)?vimeo(?:\.com)?\/(?:video\/)?(\S+)$/i,
        attrs: 'width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen',
        url: function (match) {
          return '//player.vimeo.com/video/' + match[1];
        }
      },
      {
        regex: /^\/components\/viewerjs\/index\.html#/i,
        attrs: 'width="600" height="400" frameborder="0" scrolling="no" allowfullscreen mozallowfullscreen webkitallowfullscreen',
        url: function (match) {
          return trinketConfig.getUrl(match.input);
        }
      },
      {
        regex: new RegExp('^(?:https?\\:)?\\/\\/(?:www\\.)?' + '(' + trinket_hosts.join('|') + ')' + '(?:\\/embed)?\\/(' + trinket_types.join('|') + ')(.*)', 'i'),
        attrs: 'class="embedded-trinket" width="100%" height="400" frameborder="0" scrolling="no"',
        url: function (match) {
          var type = python_types.indexOf(match[2]) >= 0 ? 'python' : match[2];
          return '//' + match[1] + '/embed/' + type + match[3];
        }
      },
      {
        regex: /^(?:https?\:)?\/\/www\.slideshare\.net\/slideshow\/embed_code\//i,
        attrs: 'width="427" height="356" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px 1px 0; margin-bottom:5px; max-width: 100%;" allowfullscreen'
      },
      {
        regex: /^(?:https?\:)?\/\/www\.google\.com\/maps\/embed/i,
        attrs: 'width="600" height="450" frameborder="0" style="border:0"'
      },
      {
        regex: /^(?:https?\:)?\/\/phet\.colorado\.edu\/sims\//i,
        attrs: 'width="800" height="600" scrolling="no"'
      }
    ];
  var HTML_WHITELIST = {
      i: { 'class': /^[a-z\-\s]+$/ },
      b: { 'class': /^[a-z\-\s]+$/ },
      u: { 'class': /^[a-z\-\s]+$/ },
      strong: { 'class': /^[a-z\-\s]+$/ },
      blockquote: { 'class': /^[a-z\-\s]+$/ },
      pre: { 'class': /^[a-z\-\s]+$/ },
      code: { 'class': /^[a-z\-\s]+$/ },
      h1: { 'class': /^[a-z\-\s]+$/ },
      h2: { 'class': /^[a-z\-\s]+$/ },
      h3: { 'class': /^[a-z\-\s]+$/ },
      h4: { 'class': /^[a-z\-\s]+$/ },
      h5: { 'class': /^[a-z\-\s]+$/ },
      h6: { 'class': /^[a-z\-\s]+$/ },
      sup: { 'class': /^[a-z\-\s]+$/ },
      sub: { 'class': /^[a-z\-\s]+$/ },
      dd: { 'class': /^[a-z\-\s]+$/ },
      dl: { 'class': /^[a-z\-\s]+$/ },
      dt: { 'class': /^[a-z\-\s]+$/ },
      ol: {
        'class': /^[a-z\-\s]+$/,
        'start': /^[0-9]+$/
      },
      ul: { 'class': /^[a-z\-\s]+$/ },
      li: { 'class': /^[a-z\-\s]+$/ },
      strike: { 'class': /^[a-z\-\s]+$/ },
      del: { 'class': /^[a-z\-\s]+$/ },
      span: { 'class': /^[a-z\-\s]+$/ },
      hr: { 'class': /^[a-z\-\s]+$/ },
      a: {
        'class': /^[a-z\-\s]+$/,
        'href': /^((https?\:)?\/\/|mailto\:)\S+$/i,
        'title': /^[^"']+$/,
        'target': /^_blank$/
      },
      p: { 'class': /^[a-z\-\s]+$/ },
      tr: { 'class': /^[a-z\-\s]+$/ },
      td: { 'class': /^[a-z\-\s]+$/ },
      th: { 'class': /^[a-z\-\s]+$/ },
      thead: { 'class': /^[a-z\-\s]+$/ },
      tbody: { 'class': /^[a-z\-\s]+$/ },
      tfoot: { 'class': /^[a-z\-\s]+$/ },
      table: {
        'class': /^[a-z\-\s]+$/,
        'width': /^\d+(px|%)?$/
      },
      img: { 'src': /^(https?\:)?\/\/docs\.google\.com\/.*drawings\//i },
      iframe: {
        align: /^(left|right|top|middle|bottom)$/i,
        frameborder: /^(0|1)$/,
        width: /^\d+(%|px)?$/,
        height: /^\d+(%|px)?$/,
        marginwidth: /^\d+$/,
        marginheight: /^\d+$/,
        scrolling: /^(no|yes|auto)$/i,
        seamless: /^seamless$/i,
        allowfullscreen: /^(allowfullscreen|true)$/i,
        webkitallowfullscreen: /^(webkitallowfullscreen|true)$/i,
        mozallowfullscreen: /^(mozallowfullscreen|true)$/i,
        style: /^(.(?!expression|javascript|\-moz\-binding))*$/i,
        src: [
          /^(https?\:)?\/\/(www\.)?youtu(be\.com|\.be)\/embed\//i,
          /^(https?\:)?\/\/(www\.)?player\.vimeo\.com\/video\//i,
          /^(https?\:)?\/\/(www\.)?google\.com\/maps\/embed/i,
          /^(https?\:)?\/\/(www\.)?slideshare\.net\/slideshow\/embed_code\//i,
          /^(https?\:)?\/\/(www\.)?geogebratube\.org\/material\/iframe\//i,
          /^(https?\:)?\/\/(www\.)?pythontutor\.com\/iframe-embed\.html/i,
          /^(https?\:)?\/\/(www\.)?screencast\-o\-matic\.com\/embed/i,
          /^(https?\:)?\/\/(www\.)?plot\.ly\/\~[\w-]+\/\d+\.embed/i,
          /^(https?\:)?\/\/docs\.google\.com\/.*(presentation|document|spreadsheets|forms)\//i,
          /^(https?\:)?\/\/linus\.highpoint\.edu/i,
          /^(https?\:)?\/\/phet\.colorado\.edu\/sims\//i,
          new RegExp('^(https?\\:)?\\/\\/(www\\.)?' + '(' + trinket_hosts.join('|') + ')' + '\\/embed\\/', 'i')
        ]
      }
    };
  var IPYNB_REGEXP = /\.ipynb$/i;
  var HTML_ATTR_REGEXP = /(?:\s+(\w+)(?:\s*=\s*(?:"(.*?)"|'(.*?)'|([^'">\s]+)))?)/gim;
  var TAGS = [];
  function escape(html, encode) {
    return html.replace(!encode ? /&(?!#?\w+;)/g : /&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }
  function sanitizeTag(tag, whitelist) {
    var attrs, foundMatch, rule;
    if (!whitelist)
      return escape(tag);
    HTML_ATTR_REGEXP.lastIndex = 0;
    while ((attrs = HTML_ATTR_REGEXP.exec(tag)) !== null) {
      foundMatch = false, rule = whitelist[attrs[1].toLowerCase()];
      var value = attrs[2] != null ? attrs[2] : attrs[3] != null ? attrs[3] : attrs[4];
      // allow whitelisted attributes with no value
      if (rule && value == null) {
        foundMatch = true;
      } else if (rule instanceof Array) {
        for (var i = 0; i < rule.length; i++) {
          if (rule[i] instanceof RegExp) {
            if (rule[i].exec(value)) {
              foundMatch = true;
              break;
            }
          }
        }
      } else if (rule instanceof RegExp && rule.exec(value)) {
        foundMatch = true;
      }
      if (!foundMatch) {
        tag = tag.substr(0, attrs.index) + tag.substr(attrs.index + attrs[0].length);
        HTML_ATTR_REGEXP.lastIndex = attrs.index;
      }
    }
    return tag;
  }
  marked.setOptions({
    sanitize: function (html) {
      var close = html.match(/^\s*<\/(\w+)\s*>\s*$/), allow = false, open, src, tagName, cleaned;
      if (close) {
        if (close[1] === TAGS[TAGS.length - 1]) {
          TAGS.pop();
          return html;
        } else {
          return escape(html);
        }
      }
      open = html.match(/^\s*<(\w+)(?:(?:\s+\w+(?:\s*=\s*(?:".*?"|'.*?'|[^'">\s]+))?)+\s*|\s*)(\/>|>)\s*$/im);
      if (!open) {
        return escape(html);
      }
      tagName = open[1].toLowerCase();
      if (HTML_WHITELIST[tagName]) {
        cleaned = sanitizeTag(html, HTML_WHITELIST[tagName]);
        if (tagName === 'iframe') {
          try {
            if ($(cleaned).attr('src')) {
              allow = true;
              html = cleaned;
            }
          } catch (e) {
          }
        } else {
          allow = true;
          html = cleaned;
        }
      }
      if (allow && open[2] === '>') {
        TAGS.push(open[1]);
      }
      return allow ? html : escape(html);
    }
  });
  window.trinketMarkdown = function (options) {
    function processCode(code, lang, escaped) {
      var output = code, parts = /^([a-zA-Z0-9]+)\.((?:run|trinket|console))(?:\:(.*))?$/.exec(lang), attrs = {
          width: '100%',
          height: '400'
        }, attrStr = '', url, arg;
      // if it matched the regex make sure it is an inline-able trinket
      if (parts && inline_trinkets.indexOf(parts[1]) == -1) {
        parts = undefined;
      }
      if (parts) {
        if (parts[3]) {
          // accept arguments of the style x=y,x="y",x='y'
          while (arg = /(\w+)=([^,]+)/.exec(parts[3])) {
            attrs[arg[1]] = arg[2].replace(/^("|')|("|')$/g, '');
            parts[3] = parts[3].substr(arg[0].length);
          }
        }
        url = trinketConfig.getUrl('/embed/' + parts[1] + '?start=result');
        if (parts[1] === 'python' && parts[2] === 'console') {
          url = url + '&runMode=console&outputOnly=true&runOption=console&leftMenu=true';
          code = code + '\n';
          // To make sure loops and functions fire
          attrs.height = 300;
        }
        if (parts[1] === 'python3' && parts[2] === 'console') {
          url = url + '&runMode=console&outputOnly=true&runOption=console&leftMenu=true';
          code = code + '\n';  // To make sure loops and functions fire
        }
        for (var key in attrs) {
          attrStr += ' ' + key + '="' + attrs[key] + '"';
        }
        url = url + '#code=' + encodeURIComponent(code);
        url = url.replace(/'/g, '%27');
        output = '<iframe class="embedded-trinket" src="' + url + '"' + attrStr + ' frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>';
      } else if (hljs.getLanguage(lang)) {
        output = '<pre><code class="hljs">' + hljs.highlight(lang, code).value + '</code></pre>';
      } else {
        output = originalCode.call(this, code, lang, escaped);
      }
      return output;
    }
    function checkForEmbedUrl(href, title, text) {
      var match;
      for (var i = 0; i < EMBED_URLS.length; i++) {
        if (match = href.match(EMBED_URLS[i].regex)) {
          return '<iframe title="' + (title || text) + '"' + ' src="' + (EMBED_URLS[i].url ? EMBED_URLS[i].url(match) : match.input) + '" ' + EMBED_URLS[i].attrs + '></iframe>';
        }
      }
      return false;
    }
    function processImage(href, title, text) {
      if (text === 'plotly') {
        var plotly_parts = href.split(':'), plotly_user = plotly_parts[0], plotly_id = plotly_parts[1], plotly_width = 640, plotly_height = 480, plotly_attr, plotly_code;
        if (/\s+=\d+(x\d+)?/.test(plotly_id)) {
          plotly_attr = /\s+=(\d+)(x(\d+))?/.exec(plotly_id);
          if (plotly_attr[1]) {
            plotly_width = plotly_attr[1];
          }
          if (plotly_attr[3]) {
            plotly_height = plotly_attr[3];
          }
          plotly_id = plotly_id.replace(/\s+=.+/, '');
        }
        plotly_code = '<iframe ' + 'width=\'' + plotly_width + '\' ' + 'height=\'' + plotly_height + '\' ' + 'frameborder=\'0\' seamless=\'seamless\' scrolling=\'no\' ' + 'src=\'https://plot.ly/~' + plotly_user + '/' + plotly_id + '/.embed' + '?width=' + plotly_width + '&height=' + plotly_height + '\'></iframe>';
        return plotly_code;
      } else {
        var embedUrl = checkForEmbedUrl(href, title, text);
        if (embedUrl) {
          return embedUrl;
        } else if (/\s+=\d+x\d*/.test(href)) {
          var attr = href.match(/\s+=(\d+)x(\d*)/);
          var width = attr[1] || '';
          // ? "width=" + attr[1] : "";
          var height = attr[2] || '';
          // ? "height=" + attr[2] : "";
          var style = '';
          var img;
          href = href.replace(attr[0], '');
          img = '<img src="' + href + '" alt="' + text + '"';
          if (width) {
            img += ' width="' + width + '"';
            style = 'style="width: ' + width + 'px;';
            if (height) {
              img += ' height="' + height + '"';
              style += ' height: ' + height + 'px"';
            } else {
              style += 'height: auto"';
            }
            img += ' style="' + style + '"';
          }
          if (title) {
            img += ' title="' + title + '"';
          }
          img += '>';
          return img;
        } else {
          return originalImage.call(this, href, title, text);
        }
      }
    }
    function processLink(href, title, text) {
      var ipynb, arg, attrs, html;
      var embed = checkForEmbedUrl(href, title, text);
      if (embed) {
        return embed;
      }
      if (/^trinket-widget$/.test(text)) {
        attrs = {};
        // accept arguments of the style x=y,x="y,z",x='y,z'
        while (arg = /(\w+)=(?:("|'|&quot;|&#39;)((?:(?=(\\?))\4.)*?)\2|()([^,]+))/.exec(href)) {
          attrs[arg[1]] = arg[3] || arg[6];
          href = href.substr(arg[0].length);
        }
        if (attrs.type) {
          attrs.type = attrs.type.toLowerCase().replace(/\s/g, '');
          switch (attrs.type) {
          case 'subscribe':
            html = '<form class="trinket-subscription-form">                <input type="email" name="email" placeholder="Email" required>                <a class="subscribe-btn button primary" data-list="' + attrs.list + '">Subscribe</a>              </form>';
            if (!options.preview) {
              window.ga && window.ga('send', 'event', 'Subscription', 'Offered', attrs.list);
              html += '<script type="text/javascript" src="' + trinketConfig.prefix('/js/plugins/trinket/subscribe.js') + '"></script>';
            }
            return html;
          }
        }
      }
      if (ipynb = href.match(IPYNB_REGEXP) && href.charAt(0) == '/') {
        return '<a href="http://nbviewer.ipython.org/urls/' + trinketConfig.get('apphostname') + href + '" title="' + title + '">' + text + '</a>';
      } else {
        var link = originalLink.call(this, href, title, text);
        if (href.charAt(0) !== '#') {
          // open links in a new window
          link = link.replace(/^<a\s/, '<a target="_blank" ');
        }
        return link;
      }
    }
    return function (src) {
      marked.Renderer.prototype.code = processCode;
      marked.Renderer.prototype.image = processImage;
      marked.Renderer.prototype.link = processLink;
      // src should be a string; replace null and undefined with empty string
      if (typeof src === 'undefined' || src == null) {
        src = '';
      }
      // check for and "protect" MathJax by adding backticks
      src = src.replace(/(\$\$|\$\(|\)\$)/g, '$1`');
      marked.Renderer.prototype.listitem = function (text) {
        if (/^\s*\[[x ]\]\s*/.test(text)) {
          text = text.replace(/^\s*\[ \]\s*/, '<input type="checkbox" class="list-item-checkbox" />').replace(/^\s*\[x\]\s*/, '<input type="checkbox" class="list-item-checkbox" checked="checked" />');
          return '<li class="list-item">' + text + '</li>';
        } else {
          return '<li>' + text + '</li>';
        }
      };
      var frameIndex = 0, iframes = [], markup = marked(src);
      // remove any code tags or backticks that were added to protect MathJax
      markup = markup.replace(/(\$\$|\$\(|\)\$)(<(?:\/)?code>|\`)/g, '$1');
      var $markup = $('<div>' + markup + '</div>');
      $markup.find('iframe').each(function (index) {
        var frame = $(this), width, height, style, host, placeholder;
        if (!frame.attr('src'))
          return;
        frame.attr('src', frame.attr('src').replace(/^https?:/, ''));
        if (options.preview) {
          // replace iframes with a placeholder in preview mode
          width = frame.attr('width') || '600';
          height = frame.attr('height') || '400';
          if (width.match(/^\d+$/))
            width += 'px';
          if (height.match(/^\d+$/))
            height += 'px';
          style = 'width:' + width + ';height:' + height + ';';
          host = frame.attr('src').match(/^(?:https?\:)?\/\/(?:www\.)?([^\/]+)/i)[1];
          placeholder = '<div class="embedded-content embed-placeholder"' + ' data-index="' + frameIndex++ + '"' + ' style="' + style + '">' + '<p>' + 'Your ' + host + ' content will display here.<br/>' + 'Click to preview.' + '</p></div>';
          iframes.push($('<div>').append(frame.clone()).html().replace(/('")/g, '\\$1'));
          frame.replaceWith(placeholder);
        } else {
          frame.addClass('embedded-content');
        }
      });
      if (options.preview && iframes.length) {
        var script = '<script type=\'text/javascript\'>\n          (function($) {\n            var iframes = [\'' + iframes.join('\',\'') + '\'];\n            $(\'.embed-placeholder\').click(function(){\n              var index = $(this).data(\'index\');\n              $(this).replaceWith(iframes[index]);\n            });\n          })(window.jQuery)\n          </script>';
        $markup.append(script);
      }
      return $markup.html();
    };
  };
}(window.hljs));(function (angular) {
  angular.module('trinket.markdown', ['trinket.config']).factory('markdownParser', [
    'trinketConfig',
    function (trinketConfig) {
      return function (options) {
        options = angular.extend({}, options);
        return trinketMarkdown(options);
      };
    }
  ]);
}(window.angular));(function (angular) {
  angular.module('trinket.util', []).factory('trinketUtil', [
    '$window',
    function ($window) {
      return {
        getProperty: function (obj, prop) {
          var path = prop.split('.');
          for (var i = 0; i < path.length; i++) {
            if (obj != null) {
              obj = obj[path[i]];
            }
          }
          return obj;
        },
        isElementVisible: function (elem, relativeTo) {
          if (!elem)
            return true;
          var off = elem.offset();
          if (!off)
            return true;
          var et = off.top;
          var eh = elem.height();
          var wh = $window.innerHeight;
          var wy = $window.pageYOffset;
          if (relativeTo && relativeTo.offset() && et < relativeTo.offset().top) {
            wy += relativeTo.offset().top;
          }
          return et >= wy && et + eh <= wh + wy;
        },
        isLarge: function () {
          return matchMedia(Foundation.media_queries['large']).matches;
        }
      };
    }
  ]).filter('formatNum', function () {
    return function (num) {
      with (Math) {
        var base = floor(log(abs(num)) / log(1000));
        var suffix = 'kmb'[base - 1];
        return suffix ? String(num / pow(1000, base)).substring(0, 3) + suffix : '' + num;
      }
    };
  }).filter('formatDate', function () {
    return function (date) {
      return moment(date).subtract(2, 'seconds').fromNow();
    };
  }).filter('localDate', function () {
    return function (date) {
      return moment(date).local().format('LLLL');
    };
  });
}(window.angular));(function (angular) {
  'use strict';
  /**
   * service for getting and posting submissions and feedback
   */
  angular.module('trinket.submissions', ['restangular']).config([
    'RestangularProvider',
    function (RestangularProvider) {
      RestangularProvider.setBaseUrl('/api');
      RestangularProvider.addResponseInterceptor(function (response) {
        return response.data ? response.data : response;
      });
      RestangularProvider.setDefaultHeaders({ 'Content-Type': 'application/json' });
    }
  ]).factory('trinketSubmissions', [
    'Restangular',
    function (Restangular) {
      var service = {};
      /**
     * sets up and starts a new "assignment"
     */
      service.startAssignment = function (material) {
        return material.customPOST({ parent: material.trinket.trinketId }, 'startAssignment');
      };
      /**
     * submits code for an "assignment"
     */
      service.submitAssignment = function (material, code, comments) {
        return material.customPOST({
          parent: material.trinket.trinketId,
          code: code,
          comments: comments
        }, 'submissions');
      };
      /**
     * updates submission in case where submission is not complete
     */
      service.updateSubmission = function (submission, code, comments) {
        var submissionElement = Restangular.restangularizeElement(null, { id: submission.id }, 'submissions');
        return submissionElement.customPOST({
          code: code,
          comments: comments
        });
      };
      /**
     * get all submissions for the current user for this material
     */
      service.getSubmissionsForMaterial = function (material) {
        var submissionElement = Restangular.restangularizeElement(null, { id: material.id }, 'submissions');
        return submissionElement.getList();
      };
      /**
     * get all submissions for this user and this material
     */
      service.getUserSubmissionsForMaterial = function (user, material) {
        var course = material.parentResource.parentResource;
        // /api/courses/{courseId}/users/{userId}/materials/{materialId}/submissions
        return Restangular.one('courses', course.id).one('users', user.userId).one('materials', material.id).all('submissions').getList();
      };
      /**
     *
     */
      service.sendFeedback = function (material, trinketId, code, feedback) {
        return material.customPOST({
          code: code,
          trinketId: trinketId,
          comments: feedback.comments,
          includeRevision: feedback.includeRevision,
          allowResubmit: feedback.allowResubmit
        }, 'feedback');
      };
      /**
     *
     */
      service.autosaveStudentComments = function (submission) {
        var submissionElement = Restangular.restangularizeElement(null, { id: submission.id }, 'comments');
        return submissionElement.customPOST({ comments: submission.comments });
      };
      /**
     *
     */
      service.autosaveFeedbackComments = function (submissionId, comments) {
        var submissionElement = Restangular.restangularizeElement(null, { id: submissionId }, 'feedback-comments');
        return submissionElement.customPOST({ comments: comments });
      };
      /**
     *
     */
      service.autosaveSubmissionOpt = function (submissionId, submissionOptKey, submissionOptVal) {
        var submissionElement = Restangular.restangularizeElement(null, { id: submissionId }, 'submission-opt'), postData = {};
        postData[submissionOptKey] = submissionOptVal;
        return submissionElement.customPOST(postData);
      };
      /**
     * updates a pending submission to submitted
     */
      service.acceptSubmission = function (material, trinketId) {
        return material.customPOST({ trinketId: trinketId }, 'acceptSubmission');
      };
      return service;
    }
  ]);
}(window.angular));(function (angular) {
  'use strict';
  angular.module('trinket.assignment', [
    'ngAria',
    'trinket.submissions',
    'trinket.util'
  ]).directive('trinketAssignment', [
    '$window',
    '$compile',
    '$templateRequest',
    '$timeout',
    '$filter',
    '$sce',
    'trinketSubmissions',
    'trinketConfig',
    'markdownParser',
    function ($window, $compile, $templateRequest, $timeout, $filter, $sce, trinketSubmissions, trinketConfig, markdownParser) {
      function link(scope, element, attrs) {
        init_scope.call(scope);
        scope.stateDateFields = {
          'submitted': 'submittedOn',
          'completed': 'submittedOn',
          'submittedLate': 'submittedOn',
          'feedback': 'lastUpdated'
        };
        var url, latestSubmission, feedbackComments;
        var parser = markdownParser({
            $scope: scope,
            preview: false
          });
        $templateRequest('/cache-prefix-28aa2534/partials/directives/trinket-assignment.html').then(function (html) {
          element.html(html);
          $compile(element.contents())(scope);
          $window.addEventListener('message', function (ev) {
            if (ev.data === 'TrinketApp ready') {
              scope.loadingAssignment = false;
              scope.assignmentVisible = true;
              if (!scope.preview && scope.allowResubmit !== false) {
                scope.canSubmit = true;
              }
              scope.$apply();
            } else if (ev.data === 'trinket.code.autosave') {
              scope.setOriginal();
            } else if (ev.data.code) {
              scope.serialized = ev.data;
              if (!ev.data._initial) {
                scope.indicateChange();
              }
            }
          });
        });
        /**
       * when a user starts an assignment
       */
        scope.startAssignment = function () {
          scope.loadingAssignment = true;
          trinketSubmissions.startAssignment(scope.material).then(function (result) {
            scope.submission.id = result.assignment.id;
            url = '/assignment-embed/' + result.assignment.lang + '/' + result.assignment.shortCode;
            set_iframe.call(scope, url);
          }, function (err) {
          });
        };
        /**
       * for preview mode
       */
        scope.showAssignment = function () {
          scope.loadingAssignment = true;
          // noStorage prevents local storage prompts/confusion
          url = '/assignment-embed-viewonly/' + scope.material.trinket.lang + '/' + scope.material.trinket.shortCode + '?noStorage=true';
          set_iframe.call(scope, url);
        };
        /**
       * when a user submits an assignment
       */
        scope.submitAssignment = function () {
          if (!scope.canSubmit || scope.submittingCode) {
            return;
          }
          scope.submittingCode = true;
          latestSubmission = null;
          angular.forEach(scope.submissions, function (submission, index) {
            if (submission.submissionState === 'submitted' || submission.submissionState === 'submittedLate') {
              latestSubmission = index;
            }
          });
          if (latestSubmission != null) {
            trinketSubmissions.updateSubmission(scope.submissions[latestSubmission], scope.serialized, scope.submission.comments).then(function (result) {
              $timeout(function () {
                scope.submissions[latestSubmission] = result.submission;
                scope.codeSubmitted = true;
                scope.isModified = false;
              }, 500);
            }, function (err) {
              if (err.status === 403) {
                // TODO: transition error display
                scope.errorMessage = err.data.message;
              } else {
              }
            }).finally(function () {
              scope.submittingCode = false;
            });
          } else {
            trinketSubmissions.submitAssignment(scope.material, scope.serialized, scope.submission.comments).then(function (result) {
              $timeout(function () {
                scope.submissions.unshift(result.submission);
                scope.submittingCode = false;
                scope.codeSubmitted = true;
                scope.isModified = false;
              }, 500);
            }, function (err) {
              if (err.status === 403) {
                // TODO: transition error display
                scope.errorMessage = err.data.message;
              } else {
              }
            });
          }
        };
        /**
       * when a user views a previous submission
       */
        scope.toggleSubmission = function (submission) {
          if (scope.showSubmission[submission.id]) {
            scope.showSubmission[submission.id] = false;
            if (submission.feedback) {
              scope.showSubmission[submission.feedback.id] = false;
            }
          } else {
            scope.showSubmission[submission.id] = true;
            if (!scope.submissionSrc[submission.id]) {
              scope.submissionSrc[submission.id] = $sce.trustAsResourceUrl(trinketConfig.getUrl('/assignment-embed-viewonly/' + submission.lang + '/' + submission.shortCode));
            }
            if (submission.feedback) {
              scope.showSubmission[submission.feedback.id] = true;
              if (!scope.submissionSrc[submission.feedback.id]) {
                scope.submissionSrc[submission.feedback.id] = $sce.trustAsResourceUrl(trinketConfig.getUrl('/assignment-embed-viewonly/' + submission.feedback.lang + '/' + submission.feedback.shortCode));
              }
            }
          }
        };
        scope.toggleOriginal = function () {
          scope.showOriginal = scope.showOriginal ? false : true;
        };
        /**
       * on initial load and anytime page changes
       */
        attrs.$observe('assignmentTrinket', function (val) {
          if (!val) {
            return;
          }
          init_scope.call(scope);
          if (!scope.preview) {
            scope.loadingAssignment = true;
            trinketSubmissions.getSubmissionsForMaterial(scope.material).then(function (submissions) {
              if (submissions.length) {
                // check status of each submission
                angular.forEach(submissions, function (submission) {
                  switch (submission.submissionState) {
                  case 'started':
                  case 'modified':
                    scope.submission.id = submission.id;
                    if (submission.comments.length && submission.comments[0].commentText.length) {
                      scope.submission.comments = submission.comments[0].commentText;
                    }
                    url = '/assignment-embed/' + submission.lang + '/' + submission.shortCode;
                    set_iframe.call(scope, url);
                    scope.original = $sce.trustAsResourceUrl(trinketConfig.getUrl('/assignment-embed-viewonly/' + scope.material.trinket.lang + '/' + scope.material.trinket.shortCode));
                    if (submission.submissionState === 'modified') {
                      scope.isModified = true;
                    }
                    break;
                  case 'submitted':
                  case 'submittedLate':
                    scope.submissions.push(submission);
                    scope.canUpdate = true;
                    break;
                  case 'completed':
                    if (scope.allowResubmit === undefined) {
                      // can student submit again
                      scope.allowResubmit = submission.allowResubmit || false;
                    }
                    if (submission.comments.length) {
                      feedbackComments = $filter('filter')(submission.comments, { commentType: 'feedback' }, true);
                      if (feedbackComments.length) {
                        submission.feedback = {
                          id: feedbackComments[0]._id,
                          lang: feedbackComments[0].trinketLang,
                          shortCode: feedbackComments[0].trinketShortCode,
                          comment: feedbackComments[0],
                          lastUpdated: feedbackComments[0].commented,
                          submissionState: 'feedback',
                          includeRevision: submission.includeRevision || false
                        };
                      }
                    }
                    scope.submissions.push(submission);
                    scope.canSubmit = false;
                    break;
                  default:
                  }
                });
              } else {
                // no "submissions" means user hasn't started yet
                scope.loadingAssignment = false;
              }
            });
          } else {
            if (scope.canEdit) {
              // link for original edit page
              scope.editLink = '/library/trinkets/' + scope.material.trinket.shortCode;
            }
          }
        });
        scope.setOriginal = function () {
          if (!scope.original) {
            scope.original = $sce.trustAsResourceUrl(trinketConfig.getUrl('/assignment-embed-viewonly/' + scope.material.trinket.lang + '/' + scope.material.trinket.shortCode));
            scope.$apply();
          }
        };
        scope.indicateChange = function () {
          scope.isModified = true;
          scope.codeSubmitted = false;
          scope.$apply();
        };
        scope.autosaveComments = function () {
          // TODO! be sure to get the latest code if scope.serialized isn't set...
          trinketSubmissions.autosaveStudentComments(scope.submission);
          scope.indicateChange();
        };
        scope.commentSrc = function (comment) {
          return $sce.trustAsResourceUrl(trinketConfig.getUrl('/assignment-embed-viewonly/' + comment.trinketLang + '/' + comment.trinketShortCode));
        };
        scope.hasDueDate = function () {
          return scope.material.trinket.submissionsDue.enabled;
        };
        scope.beforeDue = function () {
          var now = moment();
          return now < moment(scope.material.trinket.submissionsDue.dateValue);
        };
        scope.pastCutoff = function () {
          var now = moment();
          if (scope.material.trinket.submissionsCutoff.enabled && now > moment(scope.material.trinket.submissionsCutoff.dateValue)) {
            scope.canSubmit = false;
            return true;
          }
          return false;
        };
        scope.betweenDueAndCutoff = function () {
          var now = moment();
          return now > moment(scope.material.trinket.submissionsDue.dateValue) && (!scope.material.trinket.submissionsCutoff.enabled || now < moment(scope.material.trinket.submissionsCutoff.dateValue));
        };
        scope.displayFeedback = function (commentText) {
          return $sce.trustAsHtml(parser(commentText));
        };
      }
      function init_scope() {
        this.canSubmit = false;
        this.isModified = false;
        this.submitted = false;
        this.loadingAssignment = false;
        this.assignmentVisible = false;
        this.submittingCode = false;
        this.codeSubmitted = false;
        this.canUpdate = false;
        this.allowResubmit = undefined;
        this.showOriginal = false;
        this.api = null;
        this.serialized = null;
        this.original = null;
        this.submissions = [];
        this.showSubmission = {};
        this.submissionSrc = {};
        this.submission = {
          id: null,
          comments: ''
        };
        this.editLink = null;
        this.errorMessage = '';
      }
      function set_iframe(url) {
        url = trinketConfig.getUrl(url);
        // add a small diff to the URL to trigger a change and force reload
        if ($sce.valueOf(this.trinketIframe) === url) {
          url += '?diff=true';
        }
        this.trinketIframe = $sce.trustAsResourceUrl(url);
      }
      return {
        restrict: 'E',
        link: link,
        scope: {
          material: '=',
          canEdit: '=',
          preview: '=',
          assignmentTrinket: '@'
        }
      };
    }
  ]);
}(window.angular));angular.module('trinket.classPage', [
  'ngAria',
  'trinket.markdown',
  'trinket.lang',
  'ui.scrollfix',
  'restangular',
  'trinket.util',
  'trinket.assignment',
  'angularMoment'
]).config([
  'RestangularProvider',
  function (RestangularProvider) {
    RestangularProvider.setBaseUrl('/api');
    RestangularProvider.addResponseInterceptor(function (response) {
      return response.data ? response.data : response;
    });
  }
]).controller('pageControl', [
  '$scope',
  '$window',
  '$location',
  '$compile',
  '$sce',
  '$timeout',
  'markdownParser',
  'Restangular',
  'trinketUtil',
  'moment',
  function ($scope, $window, $location, $compile, $sce, $timeout, markdownParser, Restangular, trinketUtil, moment) {
    var slides = [];
    var currentSlideIndex = 0;
    var lastRenderedMaterial = null;
    var currentPath = null;
    var parser = markdownParser({
        $scope: $scope,
        preview: false
      });
    $scope.menuOpen = trinketUtil.isLarge() ? true : false;
    $scope.slides = slides;
    $scope.courseCopyName = '';
    var menu = $('#outline,#outline-expander');
    $(window).scroll(function (evt) {
      var top = window.pageYOffset || document.body.scrollTop;
      if (top <= 45 && top >= 0) {
        menu.css('top', 125 - top + 'px');
      } else {
        menu.css('top', '');
      }
    });
    $scope.$watch('courseId', function (newValue, oldValue) {
      if (!newValue)
        return;
      Restangular.one('courses', $scope.courseId).get({
        outline: true,
        with: [
          'license',
          '_owner'
        ]
      }).then(function (course) {
        $scope.course = course;
        course.lessons = Restangular.restangularizeCollection(course, course.lessons, 'lessons');
        angular.forEach(course.lessons, function (lesson) {
          lesson.materials = Restangular.restangularizeCollection(lesson, lesson.materials, 'materials');
          angular.forEach(lesson.materials, function (material) {
            slides.push({
              lesson: lesson,
              material: material
            });
          });
        });
        $scope.$on('$locationChangeSuccess', onLocationChange);
        onLocationChange();
      });
    });
    function onLocationChange() {
      var newPath = $location.path();
      if (currentPath === newPath)
        return;
      currentPath = newPath;
      var index = 0;
      if (newPath) {
        var pathString = newPath.substring(1);
        var materialPath = pathString.split('/');
        if (materialPath.length == 2) {
          for (var i = 0; i < slides.length; i++) {
            if (slides[i].lesson.slug === materialPath[0] && slides[i].material.slug === materialPath[1]) {
              index = i;
              break;
            }
          }
        }
      }
      setSlideIndex(index);
    }
    function setSlideState(index) {
      var setState = function (slide, state) {
        angular.forEach([
          'isCurrent',
          'isPast',
          'isFuture'
        ], function (property) {
          slide.material[property] = property === state;
          slide.lesson[property] = false;
        });
        if (state === 'isPast' && slide.lesson.materials[slide.lesson.materials.length - 1].id === slide.material.id) {
          slide.lesson.isPast = true;
        } else if (state === 'isFuture' && slide.lesson.materials[0].id === slide.material.id) {
          slide.lesson.isFuture = true;
        } else {
          slide.lesson.isCurrent = true;
        }
      };
      for (var i = 0; i < slides.length; i++) {
        if (i === index) {
          setState(slides[i], 'isCurrent');
        } else if (i <= index) {
          setState(slides[i], 'isPast');
        } else {
          setState(slides[i], 'isFuture');
        }
      }
    }
    function setSlideIndex(index) {
      currentSlideIndex = index;
      if (slides.length) {
        $scope.lesson = slides[currentSlideIndex].lesson;
        $scope.material = slides[currentSlideIndex].material;
      } else {
        $scope.material = { noContent: true };
        return;
      }
      setSlideState(currentSlideIndex);
      $scope.progress = (index + 1) / slides.length;
      var updateLocation = function () {
        if (!$location.path() || $location.path() === '/') {
          $location.replace();
        }
        currentPath = '/' + $scope.lesson.slug + '/' + $scope.material.slug;
        $location.path(currentPath);
      };
      var elem = $($window);
      var top = Math.min(elem.scrollTop(), 45);
      function setScroll() {
        var $outlineId = $('#' + $scope.lesson.slug + '-' + $scope.material.slug), $outline = $('#outline'), scrollTop;
        if (!trinketUtil.isElementVisible($outlineId, $outline)) {
          if ($outlineId.offset().top > $outline.offset().top) {
            scrollTop = $outline.scrollTop() + $outlineId.offset().top + $outlineId.height() - $outline.height();
          } else {
            scrollTop = $outline.scrollTop() + $outlineId.position().top - 20;
          }
          $outline.animate({ scrollTop: scrollTop }, 500);
        }
        $timeout(function () {
          elem.scrollTop(top);
        });
      }
      if ($scope.material.markup) {
        setScroll();
        return updateLocation();
      }
      $scope.material.get().then(function (material) {
        if (material.id !== $scope.material.id)
          return;
        if (typeof material.content !== 'undefined' && material.content.length) {
          $scope.material.markup = parser(material.content);
        } else {
          $scope.material.noContent = true;
        }
        setScroll();
        return updateLocation();
      });
    }
    $scope.progress = 0;
    $scope.content = function materialContent() {
      if ($scope.material && $scope.material.markup && lastRenderedMaterial !== $scope.material.id) {
        lastRenderedMaterial = $scope.material.id;
        $timeout(function () {
          MathJax.Hub.Queue([
            'Typeset',
            MathJax.Hub,
            'material'
          ]);
        });
      }
      return $sce.trustAsHtml($scope.material && $scope.material.markup || 'loading...');
    };
    $scope.goToMaterial = function goToMaterial(material) {
      for (var i = 0; i < slides.length; i++) {
        if (slides[i].material.id === material.id) {
          setSlideIndex(i);
          break;
        }
      }
    };
    $scope.haveNextMaterial = function haveNextMaterial() {
      return currentSlideIndex === slides.length - 1 ? false : true;
    };
    $scope.nextMaterial = function nextMaterial() {
      if (currentSlideIndex === slides.length - 1)
        return;
      setSlideIndex(currentSlideIndex + 1);
    };
    $scope.havePreviousMaterial = function havePreviousMaterial() {
      return currentSlideIndex === 0 ? false : true;
    };
    $scope.previousMaterial = function previousMaterial() {
      if (currentSlideIndex === 0)
        return;
      setSlideIndex(currentSlideIndex - 1);
    };
    $scope.editMaterial = function editMaterial() {
      var editLocation = $scope.course._owner.username + '/courses/' + $scope.course.slug + '#' + currentPath;
      $window.location = trinketConfig.getUrl(editLocation);
    };
    $scope.viewDashboard = function viewDashboard() {
      var dashboardLocation = $scope.course._owner.username + '/courses/' + $scope.course.slug + '#/_dashboard';
      $window.location = trinketConfig.getUrl(dashboardLocation);
    };
    $scope.copyCourse = function () {
      var name = $scope.courseCopyName || 'Copy of ' + $scope.course.name;
      return $scope.course.customPOST({ name: name }, 'copy').then(function (result) {
        if (result.success) {
          $window.location = result.url;
        } else {
          $scope.courseCopyName = name;
          $('#copyCourseNameDialog').foundation('reveal', 'open');
        }
      });
    };
    // true for students only if using a due date
    $scope.usingDates = function (material) {
      return material && material.trinket && (material.trinket.submissionsDue && material.trinket.submissionsDue.enabled);
    };
  }
]);