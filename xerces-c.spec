#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xerces-c
Version  : 3.2.4
Release  : 14
URL      : https://mirrors.advancedhosters.com/apache/xerces/c/3/sources/xerces-c-3.2.4.tar.xz
Source0  : https://mirrors.advancedhosters.com/apache/xerces/c/3/sources/xerces-c-3.2.4.tar.xz
Summary  : Validating XML parser library for C++
Group    : Development/Tools
License  : Apache-2.0
Requires: xerces-c-bin = %{version}-%{release}
Requires: xerces-c-lib = %{version}-%{release}
Requires: xerces-c-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : icu4c-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : sed
BuildRequires : zlib-dev

%description
Xerces-C++ is a validating XML parser written in a portable subset of C++.
Xerces-C++ makes it easy to give your application the ability to read and
write XML data. A shared library is provided for parsing, generating,
manipulating, and validating XML documents.

The parser provides high performance, modularity, and scalability. Source
code, samples and API documentation are provided with the parser. For
portability, care has been taken to make minimal use of templates and
minimal use of #ifdefs.

%package bin
Summary: bin components for the xerces-c package.
Group: Binaries
Requires: xerces-c-license = %{version}-%{release}

%description bin
bin components for the xerces-c package.


%package dev
Summary: dev components for the xerces-c package.
Group: Development
Requires: xerces-c-lib = %{version}-%{release}
Requires: xerces-c-bin = %{version}-%{release}
Provides: xerces-c-devel = %{version}-%{release}
Requires: xerces-c = %{version}-%{release}

%description dev
dev components for the xerces-c package.


%package lib
Summary: lib components for the xerces-c package.
Group: Libraries
Requires: xerces-c-license = %{version}-%{release}

%description lib
lib components for the xerces-c package.


%package license
Summary: license components for the xerces-c package.
Group: Default

%description license
license components for the xerces-c package.


%prep
%setup -q -n xerces-c-3.2.4
cd %{_builddir}/xerces-c-3.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666109048
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1666109048
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xerces-c
cp %{_builddir}/xerces-c-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/xerces-c/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
cp %{_builddir}/xerces-c-%{version}/NOTICE %{buildroot}/usr/share/package-licenses/xerces-c/9f30e11a37811f6763d6bd772df410c1fb72b94b || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/CreateDOMDocument
/usr/bin/DOMCount
/usr/bin/DOMPrint
/usr/bin/EnumVal
/usr/bin/MemParse
/usr/bin/PParse
/usr/bin/PSVIWriter
/usr/bin/Redirect
/usr/bin/SAX2Count
/usr/bin/SAX2Print
/usr/bin/SAXCount
/usr/bin/SAXPrint
/usr/bin/SCMPrint
/usr/bin/SEnumVal
/usr/bin/StdInParse
/usr/bin/XInclude

%files dev
%defattr(-,root,root,-)
/usr/include/xercesc/dom/DOM.hpp
/usr/include/xercesc/dom/DOMAttr.hpp
/usr/include/xercesc/dom/DOMCDATASection.hpp
/usr/include/xercesc/dom/DOMCharacterData.hpp
/usr/include/xercesc/dom/DOMComment.hpp
/usr/include/xercesc/dom/DOMConfiguration.hpp
/usr/include/xercesc/dom/DOMDocument.hpp
/usr/include/xercesc/dom/DOMDocumentFragment.hpp
/usr/include/xercesc/dom/DOMDocumentRange.hpp
/usr/include/xercesc/dom/DOMDocumentTraversal.hpp
/usr/include/xercesc/dom/DOMDocumentType.hpp
/usr/include/xercesc/dom/DOMElement.hpp
/usr/include/xercesc/dom/DOMEntity.hpp
/usr/include/xercesc/dom/DOMEntityReference.hpp
/usr/include/xercesc/dom/DOMError.hpp
/usr/include/xercesc/dom/DOMErrorHandler.hpp
/usr/include/xercesc/dom/DOMException.hpp
/usr/include/xercesc/dom/DOMImplementation.hpp
/usr/include/xercesc/dom/DOMImplementationLS.hpp
/usr/include/xercesc/dom/DOMImplementationList.hpp
/usr/include/xercesc/dom/DOMImplementationRegistry.hpp
/usr/include/xercesc/dom/DOMImplementationSource.hpp
/usr/include/xercesc/dom/DOMLSException.hpp
/usr/include/xercesc/dom/DOMLSInput.hpp
/usr/include/xercesc/dom/DOMLSOutput.hpp
/usr/include/xercesc/dom/DOMLSParser.hpp
/usr/include/xercesc/dom/DOMLSParserFilter.hpp
/usr/include/xercesc/dom/DOMLSResourceResolver.hpp
/usr/include/xercesc/dom/DOMLSSerializer.hpp
/usr/include/xercesc/dom/DOMLSSerializerFilter.hpp
/usr/include/xercesc/dom/DOMLocator.hpp
/usr/include/xercesc/dom/DOMMemoryManager.hpp
/usr/include/xercesc/dom/DOMNamedNodeMap.hpp
/usr/include/xercesc/dom/DOMNode.hpp
/usr/include/xercesc/dom/DOMNodeFilter.hpp
/usr/include/xercesc/dom/DOMNodeIterator.hpp
/usr/include/xercesc/dom/DOMNodeList.hpp
/usr/include/xercesc/dom/DOMNotation.hpp
/usr/include/xercesc/dom/DOMPSVITypeInfo.hpp
/usr/include/xercesc/dom/DOMProcessingInstruction.hpp
/usr/include/xercesc/dom/DOMRange.hpp
/usr/include/xercesc/dom/DOMRangeException.hpp
/usr/include/xercesc/dom/DOMStringList.hpp
/usr/include/xercesc/dom/DOMText.hpp
/usr/include/xercesc/dom/DOMTreeWalker.hpp
/usr/include/xercesc/dom/DOMTypeInfo.hpp
/usr/include/xercesc/dom/DOMUserDataHandler.hpp
/usr/include/xercesc/dom/DOMXPathEvaluator.hpp
/usr/include/xercesc/dom/DOMXPathException.hpp
/usr/include/xercesc/dom/DOMXPathExpression.hpp
/usr/include/xercesc/dom/DOMXPathNSResolver.hpp
/usr/include/xercesc/dom/DOMXPathNamespace.hpp
/usr/include/xercesc/dom/DOMXPathResult.hpp
/usr/include/xercesc/dom/StDOMNode.hpp
/usr/include/xercesc/dom/impl/DOMAttrImpl.hpp
/usr/include/xercesc/dom/impl/DOMAttrMapImpl.hpp
/usr/include/xercesc/dom/impl/DOMAttrNSImpl.hpp
/usr/include/xercesc/dom/impl/DOMCDATASectionImpl.hpp
/usr/include/xercesc/dom/impl/DOMCasts.hpp
/usr/include/xercesc/dom/impl/DOMCharacterDataImpl.hpp
/usr/include/xercesc/dom/impl/DOMChildNode.hpp
/usr/include/xercesc/dom/impl/DOMCommentImpl.hpp
/usr/include/xercesc/dom/impl/DOMConfigurationImpl.hpp
/usr/include/xercesc/dom/impl/DOMDeepNodeListImpl.hpp
/usr/include/xercesc/dom/impl/DOMDeepNodeListPool.c
/usr/include/xercesc/dom/impl/DOMDeepNodeListPool.hpp
/usr/include/xercesc/dom/impl/DOMDocumentFragmentImpl.hpp
/usr/include/xercesc/dom/impl/DOMDocumentImpl.hpp
/usr/include/xercesc/dom/impl/DOMDocumentTypeImpl.hpp
/usr/include/xercesc/dom/impl/DOMElementImpl.hpp
/usr/include/xercesc/dom/impl/DOMElementNSImpl.hpp
/usr/include/xercesc/dom/impl/DOMEntityImpl.hpp
/usr/include/xercesc/dom/impl/DOMEntityReferenceImpl.hpp
/usr/include/xercesc/dom/impl/DOMErrorImpl.hpp
/usr/include/xercesc/dom/impl/DOMImplementationImpl.hpp
/usr/include/xercesc/dom/impl/DOMImplementationListImpl.hpp
/usr/include/xercesc/dom/impl/DOMLSInputImpl.hpp
/usr/include/xercesc/dom/impl/DOMLSOutputImpl.hpp
/usr/include/xercesc/dom/impl/DOMLSSerializerImpl.hpp
/usr/include/xercesc/dom/impl/DOMLocatorImpl.hpp
/usr/include/xercesc/dom/impl/DOMNamedNodeMapImpl.hpp
/usr/include/xercesc/dom/impl/DOMNodeBase.hpp
/usr/include/xercesc/dom/impl/DOMNodeIDMap.hpp
/usr/include/xercesc/dom/impl/DOMNodeImpl.hpp
/usr/include/xercesc/dom/impl/DOMNodeIteratorImpl.hpp
/usr/include/xercesc/dom/impl/DOMNodeListImpl.hpp
/usr/include/xercesc/dom/impl/DOMNodeVector.hpp
/usr/include/xercesc/dom/impl/DOMNormalizer.hpp
/usr/include/xercesc/dom/impl/DOMNotationImpl.hpp
/usr/include/xercesc/dom/impl/DOMParentNode.hpp
/usr/include/xercesc/dom/impl/DOMProcessingInstructionImpl.hpp
/usr/include/xercesc/dom/impl/DOMRangeImpl.hpp
/usr/include/xercesc/dom/impl/DOMStringListImpl.hpp
/usr/include/xercesc/dom/impl/DOMStringPool.hpp
/usr/include/xercesc/dom/impl/DOMTextImpl.hpp
/usr/include/xercesc/dom/impl/DOMTreeWalkerImpl.hpp
/usr/include/xercesc/dom/impl/DOMTypeInfoImpl.hpp
/usr/include/xercesc/dom/impl/DOMXPathExpressionImpl.hpp
/usr/include/xercesc/dom/impl/DOMXPathNSResolverImpl.hpp
/usr/include/xercesc/dom/impl/DOMXPathResultImpl.hpp
/usr/include/xercesc/dom/impl/XSDElementNSImpl.hpp
/usr/include/xercesc/framework/BinOutputStream.hpp
/usr/include/xercesc/framework/LocalFileFormatTarget.hpp
/usr/include/xercesc/framework/LocalFileInputSource.hpp
/usr/include/xercesc/framework/MemBufFormatTarget.hpp
/usr/include/xercesc/framework/MemBufInputSource.hpp
/usr/include/xercesc/framework/MemoryManager.hpp
/usr/include/xercesc/framework/StdInInputSource.hpp
/usr/include/xercesc/framework/StdOutFormatTarget.hpp
/usr/include/xercesc/framework/URLInputSource.hpp
/usr/include/xercesc/framework/ValidationContext.hpp
/usr/include/xercesc/framework/Wrapper4DOMLSInput.hpp
/usr/include/xercesc/framework/Wrapper4InputSource.hpp
/usr/include/xercesc/framework/XMLAttDef.hpp
/usr/include/xercesc/framework/XMLAttDefList.hpp
/usr/include/xercesc/framework/XMLAttr.hpp
/usr/include/xercesc/framework/XMLBuffer.hpp
/usr/include/xercesc/framework/XMLBufferMgr.hpp
/usr/include/xercesc/framework/XMLContentModel.hpp
/usr/include/xercesc/framework/XMLDTDDescription.hpp
/usr/include/xercesc/framework/XMLDocumentHandler.hpp
/usr/include/xercesc/framework/XMLElementDecl.hpp
/usr/include/xercesc/framework/XMLEntityDecl.hpp
/usr/include/xercesc/framework/XMLEntityHandler.hpp
/usr/include/xercesc/framework/XMLErrorCodes.hpp
/usr/include/xercesc/framework/XMLErrorReporter.hpp
/usr/include/xercesc/framework/XMLFormatter.hpp
/usr/include/xercesc/framework/XMLGrammarDescription.hpp
/usr/include/xercesc/framework/XMLGrammarPool.hpp
/usr/include/xercesc/framework/XMLGrammarPoolImpl.hpp
/usr/include/xercesc/framework/XMLNotationDecl.hpp
/usr/include/xercesc/framework/XMLPScanToken.hpp
/usr/include/xercesc/framework/XMLRecognizer.hpp
/usr/include/xercesc/framework/XMLRefInfo.hpp
/usr/include/xercesc/framework/XMLSchemaDescription.hpp
/usr/include/xercesc/framework/XMLValidator.hpp
/usr/include/xercesc/framework/XMLValidityCodes.hpp
/usr/include/xercesc/framework/psvi/PSVIAttribute.hpp
/usr/include/xercesc/framework/psvi/PSVIAttributeList.hpp
/usr/include/xercesc/framework/psvi/PSVIElement.hpp
/usr/include/xercesc/framework/psvi/PSVIHandler.hpp
/usr/include/xercesc/framework/psvi/PSVIItem.hpp
/usr/include/xercesc/framework/psvi/XSAnnotation.hpp
/usr/include/xercesc/framework/psvi/XSAttributeDeclaration.hpp
/usr/include/xercesc/framework/psvi/XSAttributeGroupDefinition.hpp
/usr/include/xercesc/framework/psvi/XSAttributeUse.hpp
/usr/include/xercesc/framework/psvi/XSComplexTypeDefinition.hpp
/usr/include/xercesc/framework/psvi/XSConstants.hpp
/usr/include/xercesc/framework/psvi/XSElementDeclaration.hpp
/usr/include/xercesc/framework/psvi/XSFacet.hpp
/usr/include/xercesc/framework/psvi/XSIDCDefinition.hpp
/usr/include/xercesc/framework/psvi/XSModel.hpp
/usr/include/xercesc/framework/psvi/XSModelGroup.hpp
/usr/include/xercesc/framework/psvi/XSModelGroupDefinition.hpp
/usr/include/xercesc/framework/psvi/XSMultiValueFacet.hpp
/usr/include/xercesc/framework/psvi/XSNamedMap.c
/usr/include/xercesc/framework/psvi/XSNamedMap.hpp
/usr/include/xercesc/framework/psvi/XSNamespaceItem.hpp
/usr/include/xercesc/framework/psvi/XSNotationDeclaration.hpp
/usr/include/xercesc/framework/psvi/XSObject.hpp
/usr/include/xercesc/framework/psvi/XSParticle.hpp
/usr/include/xercesc/framework/psvi/XSSimpleTypeDefinition.hpp
/usr/include/xercesc/framework/psvi/XSTypeDefinition.hpp
/usr/include/xercesc/framework/psvi/XSValue.hpp
/usr/include/xercesc/framework/psvi/XSWildcard.hpp
/usr/include/xercesc/internal/BinFileOutputStream.hpp
/usr/include/xercesc/internal/BinMemOutputStream.hpp
/usr/include/xercesc/internal/CharTypeTables.hpp
/usr/include/xercesc/internal/DGXMLScanner.hpp
/usr/include/xercesc/internal/ElemStack.hpp
/usr/include/xercesc/internal/EndOfEntityException.hpp
/usr/include/xercesc/internal/IANAEncodings.hpp
/usr/include/xercesc/internal/IGXMLScanner.hpp
/usr/include/xercesc/internal/MemoryManagerImpl.hpp
/usr/include/xercesc/internal/ReaderMgr.hpp
/usr/include/xercesc/internal/SGXMLScanner.hpp
/usr/include/xercesc/internal/ValidationContextImpl.hpp
/usr/include/xercesc/internal/VecAttrListImpl.hpp
/usr/include/xercesc/internal/VecAttributesImpl.hpp
/usr/include/xercesc/internal/WFXMLScanner.hpp
/usr/include/xercesc/internal/XMLInternalErrorHandler.hpp
/usr/include/xercesc/internal/XMLReader.hpp
/usr/include/xercesc/internal/XMLScanner.hpp
/usr/include/xercesc/internal/XMLScannerResolver.hpp
/usr/include/xercesc/internal/XProtoType.hpp
/usr/include/xercesc/internal/XSAXMLScanner.hpp
/usr/include/xercesc/internal/XSObjectFactory.hpp
/usr/include/xercesc/internal/XSerializable.hpp
/usr/include/xercesc/internal/XSerializationException.hpp
/usr/include/xercesc/internal/XSerializeEngine.hpp
/usr/include/xercesc/internal/XTemplateSerializer.hpp
/usr/include/xercesc/parsers/AbstractDOMParser.hpp
/usr/include/xercesc/parsers/DOMLSParserImpl.hpp
/usr/include/xercesc/parsers/SAX2XMLFilterImpl.hpp
/usr/include/xercesc/parsers/SAX2XMLReaderImpl.hpp
/usr/include/xercesc/parsers/SAXParser.hpp
/usr/include/xercesc/parsers/XercesDOMParser.hpp
/usr/include/xercesc/sax/AttributeList.hpp
/usr/include/xercesc/sax/DTDHandler.hpp
/usr/include/xercesc/sax/DocumentHandler.hpp
/usr/include/xercesc/sax/EntityResolver.hpp
/usr/include/xercesc/sax/ErrorHandler.hpp
/usr/include/xercesc/sax/HandlerBase.hpp
/usr/include/xercesc/sax/InputSource.hpp
/usr/include/xercesc/sax/Locator.hpp
/usr/include/xercesc/sax/Parser.hpp
/usr/include/xercesc/sax/SAXException.hpp
/usr/include/xercesc/sax/SAXParseException.hpp
/usr/include/xercesc/sax2/Attributes.hpp
/usr/include/xercesc/sax2/ContentHandler.hpp
/usr/include/xercesc/sax2/DeclHandler.hpp
/usr/include/xercesc/sax2/DefaultHandler.hpp
/usr/include/xercesc/sax2/LexicalHandler.hpp
/usr/include/xercesc/sax2/SAX2XMLFilter.hpp
/usr/include/xercesc/sax2/SAX2XMLReader.hpp
/usr/include/xercesc/sax2/XMLReaderFactory.hpp
/usr/include/xercesc/util/ArrayIndexOutOfBoundsException.hpp
/usr/include/xercesc/util/Base64.hpp
/usr/include/xercesc/util/BaseRefVectorOf.c
/usr/include/xercesc/util/BaseRefVectorOf.hpp
/usr/include/xercesc/util/BinFileInputStream.hpp
/usr/include/xercesc/util/BinInputStream.hpp
/usr/include/xercesc/util/BinMemInputStream.hpp
/usr/include/xercesc/util/BitOps.hpp
/usr/include/xercesc/util/BitSet.hpp
/usr/include/xercesc/util/CountedPointer.c
/usr/include/xercesc/util/CountedPointer.hpp
/usr/include/xercesc/util/DefaultPanicHandler.hpp
/usr/include/xercesc/util/EmptyStackException.hpp
/usr/include/xercesc/util/EncodingValidator.hpp
/usr/include/xercesc/util/FileManagers/PosixFileMgr.hpp
/usr/include/xercesc/util/FlagJanitor.c
/usr/include/xercesc/util/FlagJanitor.hpp
/usr/include/xercesc/util/Hash2KeysSetOf.c
/usr/include/xercesc/util/Hash2KeysSetOf.hpp
/usr/include/xercesc/util/Hashers.hpp
/usr/include/xercesc/util/HexBin.hpp
/usr/include/xercesc/util/IOException.hpp
/usr/include/xercesc/util/IllegalArgumentException.hpp
/usr/include/xercesc/util/InvalidCastException.hpp
/usr/include/xercesc/util/Janitor.c
/usr/include/xercesc/util/Janitor.hpp
/usr/include/xercesc/util/KVStringPair.hpp
/usr/include/xercesc/util/KeyRefPair.c
/usr/include/xercesc/util/KeyRefPair.hpp
/usr/include/xercesc/util/KeyValuePair.c
/usr/include/xercesc/util/KeyValuePair.hpp
/usr/include/xercesc/util/LogicalPath.c
/usr/include/xercesc/util/MsgLoaders/InMemory/InMemMsgLoader.hpp
/usr/include/xercesc/util/MsgLoaders/InMemory/XercesMessages_en_US.hpp
/usr/include/xercesc/util/MutexManagers/StdMutexMgr.hpp
/usr/include/xercesc/util/Mutexes.hpp
/usr/include/xercesc/util/NameIdPool.c
/usr/include/xercesc/util/NameIdPool.hpp
/usr/include/xercesc/util/NetAccessors/Curl/CurlNetAccessor.hpp
/usr/include/xercesc/util/NetAccessors/Curl/CurlURLInputStream.hpp
/usr/include/xercesc/util/NoSuchElementException.hpp
/usr/include/xercesc/util/NullPointerException.hpp
/usr/include/xercesc/util/NumberFormatException.hpp
/usr/include/xercesc/util/OutOfMemoryException.hpp
/usr/include/xercesc/util/PSVIUni.hpp
/usr/include/xercesc/util/PanicHandler.hpp
/usr/include/xercesc/util/ParseException.hpp
/usr/include/xercesc/util/PlatformUtils.hpp
/usr/include/xercesc/util/QName.hpp
/usr/include/xercesc/util/RefArrayOf.c
/usr/include/xercesc/util/RefArrayOf.hpp
/usr/include/xercesc/util/RefArrayVectorOf.c
/usr/include/xercesc/util/RefArrayVectorOf.hpp
/usr/include/xercesc/util/RefHash2KeysTableOf.c
/usr/include/xercesc/util/RefHash2KeysTableOf.hpp
/usr/include/xercesc/util/RefHash3KeysIdPool.c
/usr/include/xercesc/util/RefHash3KeysIdPool.hpp
/usr/include/xercesc/util/RefHashTableOf.c
/usr/include/xercesc/util/RefHashTableOf.hpp
/usr/include/xercesc/util/RefStackOf.c
/usr/include/xercesc/util/RefStackOf.hpp
/usr/include/xercesc/util/RefVectorOf.c
/usr/include/xercesc/util/RefVectorOf.hpp
/usr/include/xercesc/util/RuntimeException.hpp
/usr/include/xercesc/util/SchemaDateTimeException.hpp
/usr/include/xercesc/util/SecurityManager.hpp
/usr/include/xercesc/util/StringPool.hpp
/usr/include/xercesc/util/SynchronizedStringPool.hpp
/usr/include/xercesc/util/TransENameMap.c
/usr/include/xercesc/util/TransENameMap.hpp
/usr/include/xercesc/util/TransService.hpp
/usr/include/xercesc/util/Transcoders/ICU/ICUTransService.hpp
/usr/include/xercesc/util/TranscodingException.hpp
/usr/include/xercesc/util/UTFDataFormatException.hpp
/usr/include/xercesc/util/UnexpectedEOFException.hpp
/usr/include/xercesc/util/UnsupportedEncodingException.hpp
/usr/include/xercesc/util/ValueArrayOf.c
/usr/include/xercesc/util/ValueArrayOf.hpp
/usr/include/xercesc/util/ValueHashTableOf.c
/usr/include/xercesc/util/ValueHashTableOf.hpp
/usr/include/xercesc/util/ValueStackOf.c
/usr/include/xercesc/util/ValueStackOf.hpp
/usr/include/xercesc/util/ValueVectorOf.c
/usr/include/xercesc/util/ValueVectorOf.hpp
/usr/include/xercesc/util/XML256TableTranscoder.hpp
/usr/include/xercesc/util/XML88591Transcoder.hpp
/usr/include/xercesc/util/XMLASCIITranscoder.hpp
/usr/include/xercesc/util/XMLAbstractDoubleFloat.hpp
/usr/include/xercesc/util/XMLBigDecimal.hpp
/usr/include/xercesc/util/XMLBigInteger.hpp
/usr/include/xercesc/util/XMLChTranscoder.hpp
/usr/include/xercesc/util/XMLChar.hpp
/usr/include/xercesc/util/XMLDOMMsg.hpp
/usr/include/xercesc/util/XMLDateTime.hpp
/usr/include/xercesc/util/XMLDouble.hpp
/usr/include/xercesc/util/XMLEBCDICTranscoder.hpp
/usr/include/xercesc/util/XMLEntityResolver.hpp
/usr/include/xercesc/util/XMLEnumerator.hpp
/usr/include/xercesc/util/XMLExceptMsgs.hpp
/usr/include/xercesc/util/XMLException.hpp
/usr/include/xercesc/util/XMLFileMgr.hpp
/usr/include/xercesc/util/XMLFloat.hpp
/usr/include/xercesc/util/XMLIBM1047Transcoder.hpp
/usr/include/xercesc/util/XMLIBM1140Transcoder.hpp
/usr/include/xercesc/util/XMLInitializer.hpp
/usr/include/xercesc/util/XMLInteger.hpp
/usr/include/xercesc/util/XMLMsgLoader.hpp
/usr/include/xercesc/util/XMLMutexMgr.hpp
/usr/include/xercesc/util/XMLNetAccessor.hpp
/usr/include/xercesc/util/XMLNumber.hpp
/usr/include/xercesc/util/XMLResourceIdentifier.hpp
/usr/include/xercesc/util/XMLString.hpp
/usr/include/xercesc/util/XMLStringTokenizer.hpp
/usr/include/xercesc/util/XMLUCS4Transcoder.hpp
/usr/include/xercesc/util/XMLURL.hpp
/usr/include/xercesc/util/XMLUTF16Transcoder.hpp
/usr/include/xercesc/util/XMLUTF8Transcoder.hpp
/usr/include/xercesc/util/XMLUni.hpp
/usr/include/xercesc/util/XMLUniDefs.hpp
/usr/include/xercesc/util/XMLUri.hpp
/usr/include/xercesc/util/XMLWin1252Transcoder.hpp
/usr/include/xercesc/util/XMemory.hpp
/usr/include/xercesc/util/XercesDefs.hpp
/usr/include/xercesc/util/XercesVersion.hpp
/usr/include/xercesc/util/Xerces_autoconf_config.hpp
/usr/include/xercesc/util/regx/ASCIIRangeFactory.hpp
/usr/include/xercesc/util/regx/BMPattern.hpp
/usr/include/xercesc/util/regx/BlockRangeFactory.hpp
/usr/include/xercesc/util/regx/CharToken.hpp
/usr/include/xercesc/util/regx/ClosureToken.hpp
/usr/include/xercesc/util/regx/ConcatToken.hpp
/usr/include/xercesc/util/regx/Match.hpp
/usr/include/xercesc/util/regx/Op.hpp
/usr/include/xercesc/util/regx/OpFactory.hpp
/usr/include/xercesc/util/regx/ParenToken.hpp
/usr/include/xercesc/util/regx/ParserForXMLSchema.hpp
/usr/include/xercesc/util/regx/RangeFactory.hpp
/usr/include/xercesc/util/regx/RangeToken.hpp
/usr/include/xercesc/util/regx/RangeTokenMap.hpp
/usr/include/xercesc/util/regx/RegularExpression.hpp
/usr/include/xercesc/util/regx/RegxDefs.hpp
/usr/include/xercesc/util/regx/RegxParser.hpp
/usr/include/xercesc/util/regx/RegxUtil.hpp
/usr/include/xercesc/util/regx/StringToken.hpp
/usr/include/xercesc/util/regx/Token.hpp
/usr/include/xercesc/util/regx/TokenFactory.hpp
/usr/include/xercesc/util/regx/TokenInc.hpp
/usr/include/xercesc/util/regx/UniCharTable.hpp
/usr/include/xercesc/util/regx/UnicodeRangeFactory.hpp
/usr/include/xercesc/util/regx/UnionToken.hpp
/usr/include/xercesc/util/regx/XMLRangeFactory.hpp
/usr/include/xercesc/util/regx/XMLUniCharacter.hpp
/usr/include/xercesc/validators/DTD/DTDAttDef.hpp
/usr/include/xercesc/validators/DTD/DTDAttDefList.hpp
/usr/include/xercesc/validators/DTD/DTDElementDecl.hpp
/usr/include/xercesc/validators/DTD/DTDEntityDecl.hpp
/usr/include/xercesc/validators/DTD/DTDGrammar.hpp
/usr/include/xercesc/validators/DTD/DTDScanner.hpp
/usr/include/xercesc/validators/DTD/DTDValidator.hpp
/usr/include/xercesc/validators/DTD/DocTypeHandler.hpp
/usr/include/xercesc/validators/DTD/XMLDTDDescriptionImpl.hpp
/usr/include/xercesc/validators/common/AllContentModel.hpp
/usr/include/xercesc/validators/common/CMAny.hpp
/usr/include/xercesc/validators/common/CMBinaryOp.hpp
/usr/include/xercesc/validators/common/CMLeaf.hpp
/usr/include/xercesc/validators/common/CMNode.hpp
/usr/include/xercesc/validators/common/CMRepeatingLeaf.hpp
/usr/include/xercesc/validators/common/CMStateSet.hpp
/usr/include/xercesc/validators/common/CMUnaryOp.hpp
/usr/include/xercesc/validators/common/ContentLeafNameTypeVector.hpp
/usr/include/xercesc/validators/common/ContentSpecNode.hpp
/usr/include/xercesc/validators/common/DFAContentModel.hpp
/usr/include/xercesc/validators/common/Grammar.hpp
/usr/include/xercesc/validators/common/GrammarResolver.hpp
/usr/include/xercesc/validators/common/MixedContentModel.hpp
/usr/include/xercesc/validators/common/SimpleContentModel.hpp
/usr/include/xercesc/validators/datatype/AbstractNumericFacetValidator.hpp
/usr/include/xercesc/validators/datatype/AbstractNumericValidator.hpp
/usr/include/xercesc/validators/datatype/AbstractStringValidator.hpp
/usr/include/xercesc/validators/datatype/AnySimpleTypeDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/AnyURIDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/Base64BinaryDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/BooleanDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/DatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/DatatypeValidatorFactory.hpp
/usr/include/xercesc/validators/datatype/DateDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/DateTimeDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/DateTimeValidator.hpp
/usr/include/xercesc/validators/datatype/DayDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/DecimalDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/DoubleDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/DurationDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/ENTITYDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/FloatDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/HexBinaryDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/IDDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/IDREFDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/InvalidDatatypeFacetException.hpp
/usr/include/xercesc/validators/datatype/InvalidDatatypeValueException.hpp
/usr/include/xercesc/validators/datatype/ListDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/MonthDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/MonthDayDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/NCNameDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/NOTATIONDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/NameDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/QNameDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/StringDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/TimeDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/UnionDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/XMLCanRepGroup.hpp
/usr/include/xercesc/validators/datatype/YearDatatypeValidator.hpp
/usr/include/xercesc/validators/datatype/YearMonthDatatypeValidator.hpp
/usr/include/xercesc/validators/schema/ComplexTypeInfo.hpp
/usr/include/xercesc/validators/schema/GeneralAttributeCheck.hpp
/usr/include/xercesc/validators/schema/NamespaceScope.hpp
/usr/include/xercesc/validators/schema/PSVIDefs.hpp
/usr/include/xercesc/validators/schema/SchemaAttDef.hpp
/usr/include/xercesc/validators/schema/SchemaAttDefList.hpp
/usr/include/xercesc/validators/schema/SchemaElementDecl.hpp
/usr/include/xercesc/validators/schema/SchemaGrammar.hpp
/usr/include/xercesc/validators/schema/SchemaInfo.hpp
/usr/include/xercesc/validators/schema/SchemaSymbols.hpp
/usr/include/xercesc/validators/schema/SchemaValidator.hpp
/usr/include/xercesc/validators/schema/SubstitutionGroupComparator.hpp
/usr/include/xercesc/validators/schema/TraverseSchema.hpp
/usr/include/xercesc/validators/schema/XMLSchemaDescriptionImpl.hpp
/usr/include/xercesc/validators/schema/XSDDOMParser.hpp
/usr/include/xercesc/validators/schema/XSDErrorReporter.hpp
/usr/include/xercesc/validators/schema/XSDLocator.hpp
/usr/include/xercesc/validators/schema/XUtil.hpp
/usr/include/xercesc/validators/schema/XercesAttGroupInfo.hpp
/usr/include/xercesc/validators/schema/XercesElementWildcard.hpp
/usr/include/xercesc/validators/schema/XercesGroupInfo.hpp
/usr/include/xercesc/validators/schema/identity/FieldActivator.hpp
/usr/include/xercesc/validators/schema/identity/FieldValueMap.hpp
/usr/include/xercesc/validators/schema/identity/IC_Field.hpp
/usr/include/xercesc/validators/schema/identity/IC_Key.hpp
/usr/include/xercesc/validators/schema/identity/IC_KeyRef.hpp
/usr/include/xercesc/validators/schema/identity/IC_Selector.hpp
/usr/include/xercesc/validators/schema/identity/IC_Unique.hpp
/usr/include/xercesc/validators/schema/identity/IdentityConstraint.hpp
/usr/include/xercesc/validators/schema/identity/IdentityConstraintHandler.hpp
/usr/include/xercesc/validators/schema/identity/ValueStore.hpp
/usr/include/xercesc/validators/schema/identity/ValueStoreCache.hpp
/usr/include/xercesc/validators/schema/identity/XPathException.hpp
/usr/include/xercesc/validators/schema/identity/XPathMatcher.hpp
/usr/include/xercesc/validators/schema/identity/XPathMatcherStack.hpp
/usr/include/xercesc/validators/schema/identity/XPathSymbols.hpp
/usr/include/xercesc/validators/schema/identity/XercesXPath.hpp
/usr/include/xercesc/xinclude/XIncludeDOMDocumentProcessor.hpp
/usr/include/xercesc/xinclude/XIncludeLocation.hpp
/usr/include/xercesc/xinclude/XIncludeUtils.hpp
/usr/lib64/pkgconfig/xerces-c.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxerces-c-3.2.so
/usr/lib64/libxerces-c.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xerces-c/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/xerces-c/9f30e11a37811f6763d6bd772df410c1fb72b94b
