from yolk.pypi import CheeseShop
import argparse
import configparser
import os

ADDON_FORMAT_STRING = "%s) %s - %s"

EXPERT_MODE = os.environ.get('PLOCK_EXPERT')
try:
    EXPERT_MODE = eval(EXPERT_MODE)
except:
    EXPERT_MODE = False

BUILDOUT_CFG = """\
[buildout]
extends = release.cfg
"""

BUILDOUT_OPT = (
    'buildout:download-cache=download-cache',
    'buildout:eggs-directory=eggs-directory',
    '-U',)

SEARCH_OPER = 'AND'
SEARCH_SPEC = {'description': 'plone', 'keyword': 'plone', 'summary': 'plone'}

argument_parser = argparse.ArgumentParser(
    description="Plock is a Plone Installer for the Pip-Loving Crowd")

argument_parser.add_argument(
    "-i", "--add-on", help="Install add-ons from PyPI", nargs="*")

argument_parser.add_argument(
    "-l", "--list-addons", action="store_true", help="List add-ons from PyPI")

argument_parser.add_argument(
    "-w", "--write-config", action="store_true", help="Write buildout.cfg")

# This option makes it possible to install addons (with --add-on) without
# completely
# replacing the current list of addons in buildout.cfg, which is the
# default behavior.
argument_parser.add_argument(
    "-p", "--preserve", action="store_true", help="Preserve add-ons")

argument_parser.add_argument(
    "-r", "--raw", action="store_true", help="Raw output")

config_parser = configparser.SafeConfigParser()

pypi = CheeseShop()

# 4.3.1-versions.cfg
_4_3_1_CFG = """\
[versions]
# ZopeApp
zope.app.applicationcontrol = 3.5.10
zope.app.appsetup = 3.14.0
zope.app.authentication = 3.8.0
zope.app.basicskin = 3.5.1
zope.app.broken = 3.6.0
zope.app.component = 3.9.3
zope.app.container = 3.9.2
zope.app.content = 3.5.1
zope.app.debug = 3.4.1
zope.app.dependable = 3.5.1
zope.app.error = 3.5.3
zope.app.exception = 3.6.3
zope.app.folder = 3.5.2
zope.app.form = 4.0.2
zope.app.generations = 3.6.1
zope.app.http = 3.9.0
zope.app.i18n = 3.6.4
zope.app.locales = 3.6.2
zope.app.localpermission = 3.7.2
zope.app.pagetemplate = 3.11.2
zope.app.principalannotation = 3.7.0
zope.app.publication = 3.12.0
zope.app.publisher = 3.10.2
zope.app.renderer = 3.5.1
zope.app.rotterdam = 3.5.3
zope.app.schema = 3.5.0
zope.app.security = 3.7.5
# zope.app.testing branch which is compatible with zope.testbrowser 3.8.
zope.app.testing = 3.7.8
zope.app.wsgi = 3.9.3
zope.app.zcmlfiles = 3.7.1
zope.app.zopeappgenerations = 3.5.1
roman = 1.4.0
wsgi-intercept = 0.4
zc.sourcefactory = 0.7.0
# Next major version of zope.testbrowser fails on py24.
zope.testbrowser = 3.8.2

# Deprecating
zodbcode = 3.4.0
zope.app.apidoc = 3.7.5
zope.app.cache = 3.7.0
zope.app.catalog = 3.8.1
zope.app.dav = 3.5.3
zope.app.debugskin = 3.4.1
zope.app.file = 3.6.1
zope.app.ftp = 3.5.0
zope.app.interface = 3.5.2
zope.app.interpreter = 3.4.0
zope.app.intid = 3.7.1
zope.app.keyreference = 3.6.1
zope.app.locking = 3.5.0
zope.app.onlinehelp = 3.5.2
zope.app.preference = 3.8.1
zope.app.preview = 3.4.0
zope.app.securitypolicy = 3.6.1
zope.app.server = 3.6.0
zope.app.session = 3.6.2
zope.app.skins = 3.4.0
zope.app.tree = 3.6.0
zope.app.twisted = 3.5.0
zope.app.undo = 3.5.0
zope.app.zptpage = 3.5.1
zope.file = 0.6.2
zope.html = 2.1.0
zope.modulealias = 3.4.0
zope.preference = 3.8.0
zope.thread = 3.4
zope.xmlpickle = 3.4.0
zope.rdb = 3.5.0

# ZTK
zope.annotation = 3.5.0
zope.applicationcontrol = 3.5.5
zope.authentication = 3.7.1
zope.broken = 3.6.0
zope.browser = 1.3
zope.browsermenu = 3.9.1
zope.browserpage = 3.12.2
zope.browserresource = 3.10.3
zope.cachedescriptors = 3.5.1
zope.catalog = 3.8.2
zope.component = 3.9.5
zope.componentvocabulary = 1.0.1
zope.configuration = 3.7.4
zope.container = 3.11.2
zope.contentprovider = 3.7.2
zope.contenttype = 3.5.5
zope.copy = 3.5.0
zope.copypastemove = 3.7.0
zope.datetime = 3.4.1
zope.deferredimport = 3.5.3
zope.deprecation = 3.4.1
zope.dottedname = 3.4.6
zope.dublincore = 3.7.0
zope.error = 3.7.4
zope.event = 3.5.2
zope.exceptions = 3.6.2
zope.filerepresentation = 3.6.1
zope.formlib = 4.0.6
zope.hookable = 3.4.1
zope.i18n = 3.7.4
zope.i18nmessageid = 3.5.3
zope.index = 3.6.4
zope.interface = 3.6.7
zope.intid = 3.7.2
zope.keyreference = 3.6.4
zope.lifecycleevent = 3.6.2
zope.location = 3.9.1
zope.login = 1.0.0
zope.mimetype = 1.3.1
zope.minmax = 1.1.2
zope.pagetemplate = 3.5.2
zope.password = 3.6.1
zope.pluggableauth = 1.0.3
zope.principalannotation = 3.6.1
zope.principalregistry = 3.7.1
zope.processlifetime = 1.0
zope.proxy = 3.6.1
zope.ptresource = 3.9.0
zope.publisher = 3.12.6
zope.ramcache = 1.0
zope.schema = 3.7.1
zope.security = 3.7.4
zope.securitypolicy = 3.7.0
zope.sendmail = 3.7.5
zope.sequencesort = 3.4.0
zope.server = 3.6.3
zope.session = 3.9.5
zope.site = 3.9.2
zope.size = 3.4.1
zope.structuredtext = 3.5.1
zope.tal = 3.5.2
zope.tales = 3.5.3
zope.testing = 3.9.7
zope.traversing = 3.13.2
zope.viewlet = 3.7.2

# Deprecating
zope.documenttemplate = 3.4.3

# Dependencies
# Needed for the mechanize 0.1.x.
ClientForm = 0.2.10
distribute = 0.6.36
docutils = 0.7
Jinja2 = 2.5.5
# Newer versions of mechanize are not fully py24 compatible.
mechanize = 0.1.11
Paste = 1.7.5.1
PasteDeploy = 1.3.4
PasteScript = 1.7.5
py = 1.3.4
Pygments = 1.3.1
python-gettext = 1.0
pytz = 2013b
RestrictedPython = 3.6.0
setuptools = 0.6c11
Sphinx = 1.0.8
transaction = 1.1.1
unittest2 = 0.5.1
z3c.recipe.sphinxdoc = 0.0.8
zc.buildout = 1.7.1
zc.lockfile = 1.0.2
ZConfig = 2.8.0
zc.recipe.egg = 1.3.2
zc.recipe.testrunner = 1.2.1
zc.resourcelibrary = 1.3.4
zdaemon = 2.0.7
ZODB3 = 3.9.7
zope.mkzeoinstance = 3.9.5

# toolchain
argparse = 1.1
coverage = 3.5.2
lxml = 2.2.8
mr.developer = 1.25
tl.eggdeps = 0.4
nose = 1.1.2
z3c.checkversions = 0.4.1
z3c.recipe.compattest = 0.12.2
z3c.recipe.depgraph = 0.5
zope.kgs = 1.2.0

# Zope2-specific
Zope2 = 2.13.20
AccessControl = 2.13.11
Acquisition = 2.13.8
DateTime = 2.12.7
DocumentTemplate = 2.13.2
ExtensionClass = 2.13.2
initgroups = 2.13.0
Missing = 2.13.1
MultiMapping = 2.13.0
nt-svcutils = 2.13.0
Persistence = 2.13.2
Products.BTreeFolder2 = 2.13.4
Products.ExternalMethod = 2.13.0
Products.MailHost = 2.13.1
Products.MIMETools = 2.13.0
Products.OFSP = 2.13.2
Products.PythonScripts = 2.13.2
Products.StandardCacheManagers = 2.13.0
Products.ZCatalog = 2.13.23
Products.ZCTextIndex = 2.13.4
Record = 2.13.0
tempstorage = 2.12.2
zExceptions = 2.13.0
zLOG = 2.11.1
ZopeUndo = 2.12.0

# ZTK KGS overrides
manuel = 1.1.1
mechanize = 0.2.5
python-gettext = 1.2
ZConfig = 2.9.1
ZODB3 = 3.10.5

# Zope2 dependencies
repoze.retry = 1.2
repoze.tm2 = 1.0
repoze.who = 2.0
zope.testbrowser = 3.11.1

# Zope overrides
docutils = 0.9.1
# Get support for @security decorators
AccessControl = 3.0.6
# More memory efficient version, Trac #13101
DateTime = 3.0.3
# Products.BTreeFolder2 2.13.4 causes a regression
Products.BTreeFolder2 = 2.13.3
# Override until ztk is updated
Sphinx = 1.1.3
# required for recent z3c.form and chameleon
zope.pagetemplate = 3.6.3

# Build tools
buildout.dumppickedversions = 0.5
collective.recipe.omelette = 0.15
collective.recipe.template = 1.9
#collective.xmltestreport = 1.3.0
decorator = 3.4.0
distribute = 0.6.28
mr.developer = 1.21
plone.recipe.alltests = 1.2
plone.recipe.zope2instance = 4.2.11
plone.recipe.zeoserver = 1.2.5
robotframework = 2.7.6
robotframework-selenium2library = 1.1.0
robotsuite = 1.2.1
selenium = 2.31.0
setuptools = 0.6c11
z3c.coverage = 1.2.0
z3c.ptcompat = 1.0.1
z3c.template = 1.4.1
zest.releaser = 3.43
zope.testrunner = 4.1.1

# External dependencies
Markdown = 2.0.3
PIL = 1.1.7
Pillow = 1.7.8
# Unidecode 0.04.{2-9} break tests
Unidecode = 0.04.1
elementtree = 1.2.7-20070827-preview
experimental.cssselect = 0.3
feedparser = 5.0.1
lxml = 2.3.6
mailinglogger = 3.7.0
ordereddict = 1.1
python-dateutil = 1.5
python-openid = 2.2.5
repoze.xmliter = 0.5
simplejson = 2.5.2
six = 1.2.0
WebOb = 1.0.8


# Plone release
Plone                                 = 4.3.1
Products.ATContentTypes               = 2.1.13
Products.ATReferenceBrowserWidget     = 3.0
Products.Archetypes                   = 1.9.1
Products.CMFActionIcons               = 2.1.3
Products.CMFCalendar                  = 2.2.2
Products.CMFCore                      = 2.2.7
Products.CMFDefault                   = 2.2.3
Products.CMFDiffTool                  = 2.1
Products.CMFDynamicViewFTI            = 4.0.5
Products.CMFEditions                  = 2.2.8
Products.CMFFormController            = 3.0.3
Products.CMFPlacefulWorkflow          = 1.5.9
Products.CMFPlone                     = 4.3.1
Products.CMFQuickInstallerTool        = 3.0.6
Products.CMFTestCase                  = 0.9.12
Products.CMFTopic                     = 2.2.1
Products.CMFUid                       = 2.2.1
Products.contentmigration             = 2.1.4
Products.DCWorkflow                   = 2.2.4
Products.ExtendedPathIndex            = 3.1
Products.ExternalEditor               = 1.1.0
Products.GenericSetup                 = 1.7.3
Products.Marshall                     = 2.1.2
Products.MimetypesRegistry            = 2.0.4
Products.PasswordResetTool            = 2.0.14
Products.PlacelessTranslationService  = 2.0.3
Products.PloneLanguageTool            = 3.2.7
Products.PlonePAS                     = 4.1.1
Products.PloneTestCase                = 0.9.17
Products.PluggableAuthService         = 1.10.0
Products.PluginRegistry               = 1.3
Products.PortalTransforms             = 2.1.2
Products.ResourceRegistries           = 2.2.9
Products.SecureMailHost               = 1.1.2
Products.TinyMCE                      = 1.3.4
Products.ZopeVersionControl           = 1.1.3
Products.ZSQLMethods                  = 2.13.4
Products.i18ntestcase                 = 1.3
Products.statusmessages               = 4.0
Products.validation                   = 2.0
archetypes.querywidget                = 1.0.8
archetypes.referencebrowserwidget     = 2.4.18
archetypes.schemaextender             = 2.1.2
borg.localrole                        = 3.0.2
collective.monkeypatcher              = 1.0.1
collective.testcaselayer              = 1.6
collective.z3cform.datetimewidget     = 1.2.3
diazo                                 = 1.0.3
five.customerize                      = 1.1
five.formlib                          = 1.0.4
five.globalrequest                    = 1.0
five.localsitemanager                 = 2.0.5
plone.app.blob                        = 1.5.8
plone.app.caching                     = 1.1.4
plone.app.collection                  = 1.0.10
plone.app.content                     = 2.1.2
plone.app.contentlisting              = 1.0.4
plone.app.contentmenu                 = 2.0.8
plone.app.contentrules                = 3.0.3
plone.app.controlpanel                = 2.3.6
plone.app.customerize                 = 1.2.2
plone.app.dexterity                   = 2.0.8
plone.app.discussion                  = 2.2.6
plone.app.folder                      = 1.0.5
plone.app.form                        = 2.2.2
plone.app.i18n                        = 2.0.2
plone.app.imaging                     = 1.0.9
plone.app.iterate                     = 2.1.10
plone.app.jquery                      = 1.7.2
plone.app.jquerytools                 = 1.5.5
plone.app.layout                      = 2.3.5
plone.app.linkintegrity               = 1.5.2
plone.app.locales                     = 4.3.1
plone.app.openid                      = 2.0.2
plone.app.portlets                    = 2.4.4
plone.app.querystring                 = 1.0.8
plone.app.redirector                  = 1.2
plone.app.registry                    = 1.2.3
plone.app.search                      = 1.1.4
plone.app.testing                     = 4.2.2
plone.app.textfield                   = 1.2.2
plone.app.theming                     = 1.1.1
plone.app.upgrade                     = 1.3.3
plone.app.users                       = 1.2a2
plone.app.uuid                        = 1.0
plone.app.viewletmanager              = 2.0.3
plone.app.vocabularies                = 2.1.10
plone.app.workflow                    = 2.1.5
plone.app.z3cform                     = 0.7.3
plone.alterego                        = 1.0
plone.autoform                        = 1.4
plone.batching                        = 1.0
plone.behavior                        = 1.0.2
plone.browserlayer                    = 2.1.2
plone.cachepurging                    = 1.0.4
plone.caching                         = 1.0
plone.contentrules                    = 2.0.3
plone.dexterity                       = 2.1.3
plone.fieldsets                       = 2.0.2
plone.folder                          = 1.0.4
plone.formwidget.namedfile            = 1.0.6
plone.i18n                            = 2.0.8
plone.indexer                         = 1.0.2
plone.intelligenttext                 = 2.0.2
plone.keyring                         = 2.0.1
plone.locking                         = 2.0.4
plone.memoize                         = 1.1.1
plone.namedfile                       = 2.0.2
plone.openid                          = 2.0.1
plone.outputfilters                   = 1.10
plone.portlet.collection              = 2.1.5
plone.portlet.static                  = 2.0.2
plone.portlets                        = 2.2
plone.protect                         = 2.0.2
plone.registry                        = 1.0.1
plone.reload                          = 2.0
plone.resource                        = 1.0.2
plone.resourceeditor                  = 1.0
plone.rfc822                          = 1.0.1
plone.scale                           = 1.3.2
plone.schemaeditor                    = 1.3.2
plone.session                         = 3.5.3
plone.stringinterp                    = 1.0.10
plone.subrequest                      = 1.6.7
plone.supermodel                      = 1.2.2
plone.synchronize                     = 1.0.1
plone.testing                         = 4.0.8
plone.theme                           = 2.1
plone.transformchain                  = 1.0.3
plone.uuid                            = 1.0.3
plone.z3cform                         = 0.8.0
plonetheme.classic                    = 1.3.2
plonetheme.sunburst                   = 1.4.4
rwproperty                            = 1.0
wicked                                = 1.1.10
z3c.autoinclude                       = 0.3.4
z3c.batching                          = 1.1.0
z3c.blobfile                          = 0.1.5
z3c.caching                           = 2.0a1
z3c.form                              = 3.0
z3c.formwidget.query                  = 0.9
z3c.zcmlhook                          = 1.0b1
zope.globalrequest                    = 1.0
zope.schema                           = 4.2.2

# Ecosystem (not officially part of core)
collective.js.jqueryui                = 1.10.1.2
collective.z3cform.datagridfield      = 0.11
collective.z3cform.datagridfield-demo = 0.5
five.grok                             = 1.3.2
five.intid                            = 1.0.3
grokcore.annotation                   = 1.3
grokcore.component                    = 2.5
grokcore.formlib                      = 1.9
grokcore.security                     = 1.6.2
grokcore.site                         = 1.6.1
grokcore.view                         = 2.7
grokcore.viewlet                      = 1.10.1
martian                               = 0.14
mocker                                = 1.1.1
plone.app.intid                       = 1.0.2
plone.app.lockingbehavior             = 1.0.1
plone.app.referenceablebehavior       = 0.5
plone.app.relationfield               = 1.2.1
plone.app.stagingbehavior             = 0.1b4
plone.app.versioningbehavior          = 1.1
plone.directives.dexterity            = 1.0.2
plone.directives.form                 = 2.0
plone.formwidget.autocomplete         = 1.2.4
plone.formwidget.contenttree          = 1.0.6
plone.mocktestcase                    = 1.0b3
z3c.objpath                           = 1.1
z3c.relationfield                     = 0.6.2
zc.relation                           = 1.0
"""

# base.cfg
BASE_CFG = """\
[buildout]
allow-hosts =
    *.plone.org
    *.python.org
find-links =
    http://dist.plone.org/thirdparty/docutils-0.9.1.tar.gz
    http://dist.plone.org/thirdparty/elementtree-1.2.7-20070827-preview.zip
parts = plone

[base]
packages =
    Pillow
    Plone

[plone]
eggs =
    ${base:packages}
products =
recipe = plone.recipe.zope2instance
user = admin:admin
zcml =

[versions]
# Avoid templer
ZopeSkel = 2.21.2

# Use latest; i.e higher versions than Plone core uses
Pillow = 2.1.0
zc.buildout = 2.2.0
setuptools = 0.9.8
"""

# release.cfg
RELEASE_CFG = """\
[buildout]
extends =
    4.3.1-versions.cfg
    base.cfg

[plone]
eggs =
    ${base:packages}
    ${version:packages}

zcml +=
    zope2_bootstrap

[version]
packages =
    plonetheme.diazo_sunburst
    zope2_bootstrap
"""
