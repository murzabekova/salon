header('Access-Control-Allow-Origin: *');
function miniCalendar(parentEl, cfg) {
  var year, month, day, sel, mode, dayEls, allowedDays, offset, auto, lock
    , minDate
    , parentEl = $(parentEl)
    , dateTitleEl = parentEl.find('.calendar-mini-date-title')
    , monthTitleEl = parentEl.find('.calendar-mini-month-title')
    , menuEl = parentEl.find('.btn-group')
    , bodyEl = parentEl.find('.calendar-mini-body')
    , prevEl = parentEl.find('.calendar-mini-prev')
    , nextEl = parentEl.find('.calendar-mini-next')
    , todayEl = parentEl.find('.calendar-mini-today')
    , lang = $(document.body).data('lang');

  mode = cfg.mode || 'day';

  function setDate(date, force) {
    date = date || (new Date());

    day = date.getDate();
    month = date.getMonth();
    year = date.getFullYear();

    sel = [ year, month, day ];

    render(force ? false : true);
    hide();
  }

  function compareDate() {
    var m = minDate.getMonth()
      , y = minDate.getFullYear();

    if (year != y) {
      return year - y;
    }
    else if (month != m) {
      return month - m;
    }
    else {
      return 0;
    }
  }

  function setDateC(y, m, d, force) {
    var date = new Date(y, m - 1, d);
    setDate(date, force);
  }

  function setDateF(fmt, force) {
    var ymd = fmt.split('-')
      , date = new Date(ymd[ 0 ], ymd[ 1 ] - 1, ymd[ 2 ]);
    setDate(date, force);
  }

  function pad(v) {
    v = parseInt(v, 10) || 0;
    return String(v < 10 ? ('0' + v) : v);
  }

  function getDate() {
    return sel[ 0 ].toString() + '-' + pad(sel[ 1 ] + 1) + '-' + pad(sel[ 2 ]);
  }

  function getDateObj() {
    return new Date(sel[ 0 ], sel[ 1 ], sel[ 2 ]);
  }

  function renderDay(num, cls) {
    var el = $('<div class="day"></div>').text(num)
      , nr = (offset % 7) || 0;

    if (allowedDays) {
      el.toggleClass('day-disabled', cls || !allowedDays[ num ]);
    }

    cls = cls || num;
    el.addClass('day-' + cls);
    el.appendTo(bodyEl);

    offset++;
  }

  function formatDay(day) {
    if (lang == 'lv') {
      day = day + '.';
    }

    return day;
  }

  function setAllowedDays(days) {
    allowedDays = days;
    render();
  }

  function checkPrevState() {
    if (minDate) {
      prevEl.toggleClass('disabled', compareDate() <= 0);
    }
  }

  function autoSelect() {
    var els = bodyEl.find('.day:not(.day-disabled)');

    if (els.length) {
      auto = true;
      lock = false;
      $(els.get(0)).click();
    }
    else if (!lock) {
      lock = true;
      nextEl.click();
    }

    checkPrevState();
  }

  function setMinTS(ts) {
    minDate = new Date(ts * 1000);
    setDate();
    render();

    if (cfg.prevNextCb) {
      cfg.prevNextCb(year, month);
    }
  }

  function getTitle() {
    var date = new Date(year, month, day)
      , ds = date.getDay() || 7
      , title, sday, eday, smonth, emonth;

    if (mode == 'week') {
      date = new Date(year, month, day - ds + 1);
      sday = date.getDate();
      smonth = date.getMonth();

      date = new Date(year, month, day - ds + 7);
      eday = date.getDate();
      emonth = date.getMonth();

      if (smonth == emonth) {
        title = formatDay(sday) + ' - ' + formatDay(eday) + ' ' + cfg.monthNamesAlt[ smonth ];
      }
      else {
        title = formatDay(sday) + ' ' + cfg.monthNamesAlt[ smonth ] + ' - ';
        title += formatDay(eday) + ' ' + cfg.monthNamesAlt[ emonth ];
      }
    }
    else {
      if (cfg.dayNames) {
        title = formatDay(day) + ' ' + cfg.monthNamesAlt[ month ] + ', ' + cfg.dayNames[ ds ];
      }
      else {
        title = pad(day) + '.' + pad(month + 1) + '.' + year.toString();
      }
    }

    return title.toLowerCase();
  }

  function setTitle() {
    title = getTitle();
    dateTitleEl.text(title);
  }

  function setMode(m) {
    mode = m;
    hide();
    select();
  }

  function render(supress) {
    var date = new Date(year, month + 1, 0)
      , dn, dp, ds, dc, i, cls;

    dayEls && dayEls.remove();

    dn = date.getDate();
    date.setDate(1);
    ds = date.getDay() || 7;
    dp = (new Date(year, month, 0)).getDate();

    offset = 1;

    for (i = 1; i < ds; i++) {
      renderDay(dp - ds + i + 1, 'prev');
    }

    for (i = 1; i <= dn; i++) {
      renderDay(i);
    }

    dc = 7 - (ds + dn - 1) % 7;
    for (i = 1; i <= dc % 7; i++) {
      renderDay(i, 'next');
    }

    dayEls = bodyEl.find('.day');
    monthTitleEl.text(cfg.monthNames[ month ] + ' ' + year);

    if (year == sel[ 0 ] && month == sel[ 1 ]) {
      select(supress);
    }

    checkPrevState();
  }

  function select(supress) {
    var days = bodyEl.find('.day')
      , cls = 'day-' + day
      , pos = -1, spos, epos;

    sel = [ year, month, day ];
    days.removeClass('active');

    if (mode == 'week') {
      days.each(function(index, el) {
        el = $(el);
        if (el.hasClass(cls)) {
          pos = index;
        }
      });

      if (pos < 0) {
        return;
      }

      spos = pos - (pos % 7);
      epos = spos + 6;
      days.each(function(index, el) {
        if (index <= epos && spos <= index) {
          $(el).addClass('active');
        }
      });
    }
    else {
      bodyEl.find('.' + cls).addClass('active');
    }

    if (!supress && cfg.callback) {
      cfg.callback.apply(null, sel);
    }

    setTitle();
  }

  function hide() {
    menuEl.removeClass('open');
  }

  prevEl.click(function() {
    if (minDate && compareDate() < 0) {
      return;
    }

    if (month == 0) {
      month = 11;
      year--;
    }
    else {
      month--;
    }

    render(true);
    if (cfg.prevNextCb) {
      cfg.prevNextCb(year, month);
    }
  });

  nextEl.click(function() {
    if (month == 11) {
      month = 0;
      year++;
    }
    else {
      month++;
    }

    render(true);
    if (cfg.prevNextCb) {
      cfg.prevNextCb(year, month);
    }
  });

  bodyEl.on('click', '.day', function(e) {
    var el = $(e.currentTarget)
      , d = parseInt(el.text(), 10);

    if (el.hasClass('day-disabled')) {
      return;
    }
    else if (el.hasClass('day-prev')) {
      prevEl.trigger('click');
      bodyEl.find('.day-' + d).trigger('click');
    }
    else if (el.hasClass('day-next')) {
      nextEl.trigger('click');
      bodyEl.find('.day-' + d).trigger('click');
    }
    else {
      day = d;
      select();

      if (auto) {
        auto = false;
      }
      else {
        hide();
      }
    }
  });

  todayEl.click(function() {
    setDate();

    if (cfg.callback) {
      cfg.callback.apply(null, sel);
    }
  });

  this.setDate = setDate;
  this.setDateC = setDateC;
  this.setDateF = setDateF;
  this.getDate = getDate;
  this.getDateObj = getDateObj;
  this.getTitle = getTitle;
  this.setMode = setMode;
  this.setMinTS = setMinTS;
  this.setAllowedDays = setAllowedDays;
  this.autoSelect = autoSelect;
  this.hide = hide;

  setDate();
}
