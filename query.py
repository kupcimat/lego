VARIABLES = {
    "page": 1,
    "isPaginated": False,
    "perPage": 18,
    "sort": {"key": "FEATURED", "direction": "DESC"},
    "filters": [],
    "slug": "/categories/new-sets-and-products",
}

QUERY = """query ContentPageQuery($slug: String!, $perPage: Int, $page: Int, $isPaginated: Boolean!, $sort: SortInput, $filters: [Filter!]) {
  contentPage(slug: $slug) {
    id
    analyticsGroup
    analyticsPageTitle
    metaTitle
    metaDescription
    metaOpenGraph {
      title
      description
      imageUrl
      __typename
    }
    url
    title
    displayTitleOnPage
    ...Breadcrumbs
    sections {
      ... on LayoutSection {
        ...PageLayoutSection
        __typename
      }
      ...ContentSections
      ... on TargetedSection {
        fetchOnClient
        section {
          ...ContentSections
          ... on LayoutSection {
            ...PageLayoutSection
            __typename
          }
          ... on ProductCarouselSection {
            ...ProductCarousel_UniqueFields
            productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {
              ...Product_ProductItem
              __typename
            }
            __typename
          }
          __typename
        }
        __typename
      }
      ... on SplitTestingSection {
        variantId
        testId
        optimizelyEntityId
        inExperimentAudience
        section {
          ...ContentSections
          ... on LayoutSection {
            ...PageLayoutSection
            __typename
          }
          ... on ProductCarouselSection {
            ...ProductCarousel_UniqueFields
            productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {
              ...Product_ProductItem
              __typename
            }
            __typename
          }
          __typename
        }
        __typename
      }
      ... on ProductSection {
        removePadding
        ... on DisruptorProductSection {
          ...DisruptorSection
          __typename
        }
        ... on CountdownProductSection {
          ...CountdownSection
          __typename
        }
        products(perPage: $perPage, page: $page, sort: $sort, filters: $filters) @include(if: $isPaginated) {
          ...ProductListings
          __typename
        }
        products(page: $page, perPage: $perPage, sort: $sort, filters: $filters) @skip(if: $isPaginated) {
          ...ProductListings
          __typename
        }
        __typename
      }
      ... on ProductCarouselSection {
        ...ProductCarousel_UniqueFields
        productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {
          ...Product_ProductItem
          __typename
        }
        __typename
      }
      ... on CustomProductCarouselSection {
        ...CustomProductCarousel_UniqueFields
        productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {
          ...CustomProductCarousel_ItemFields
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment ContentSections on ContentSection {
  __typename
  id
  ...UserGeneratedContentData
  ...AccordionSectionData
  ...BreadcrumbSection
  ...CategoryListingSection
  ...ListingBannerSection
  ...CardContentSection
  ...CardCarouselSection
  ...CopyContent
  ...CopySectionData
  ...QuickLinksData
  ...ContentBlockMixedData
  ...HeroBannerData
  ...MotionBannerData
  ...MotionSidekickData
  ...InPageNavData
  ...GalleryData
  ...TableData
  ...RecommendationSectionData
  ...SidekickBannerData
  ...TextBlockData
  ...TextBlockSEOData
  ...CountdownBannerData
  ...CrowdTwistWidgetSection
  ...CodedSection
  ...GridSectionData
  ...StickyCTAData
  ...AudioSectionData
  ...MotionSidekick1x1Data
  ...ImageTransitionSliderData
  ...PollsSectionData
  ...ArtNavigationData
}

fragment AccordionSectionData on AccordionSection {
  __typename
  title
  showTitle
  accordionblocks {
    title
    text
    __typename
  }
}

fragment PageLayoutSection on LayoutSection {
  __typename
  id
  backgroundColor
  removePadding
  fullWidth
  innerSection: section {
    id
    ...ContentSections
    ... on ProductCarouselSection {
      ...ProductCarousel_UniqueFields
      productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {
        ...Product_ProductItem
        __typename
      }
      __typename
    }
    ... on CustomProductCarouselSection {
      ...CustomProductCarousel_UniqueFields
      productCarouselProducts: products(page: 1, perPage: 16, sort: $sort) {
        ...CustomProductCarousel_ItemFields
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment BreadcrumbSection on BreadcrumbSection {
  ...BreadcrumbDynamicSection
  __typename
}

fragment BreadcrumbDynamicSection on BreadcrumbSection {
  breadcrumbs {
    label
    url
    analyticsTitle
    __typename
  }
  __typename
}

fragment ListingBannerSection on ListingBannerSection {
  ...ListingBanner
  __typename
}

fragment ListingBanner on ListingBannerSection {
  title
  description
  contrast
  logoImage
  backgroundImages {
    small {
      ...ImageAsset
      __typename
    }
    medium {
      ...ImageAsset
      __typename
    }
    large {
      ...ImageAsset
      __typename
    }
    __typename
  }
  __typename
}

fragment ImageAsset on ImageAssetDetails {
  url
  width
  height
  maxPixelDensity
  format
  __typename
}

fragment CategoryListingSection on CategoryListingSection {
  ...CategoryListing
  __typename
}

fragment CategoryListing on CategoryListingSection {
  title
  description
  thumbnailImage
  children {
    ...CategoryLeafSection
    __typename
  }
  __typename
}

fragment CategoryLeafSection on CategoryListingChildren {
  title
  description
  thumbnailImage
  logoImage
  url
  ageRange
  tag
  thumbnailSrc {
    ...ImageAsset
    __typename
  }
  __typename
}

fragment DisruptorSection on DisruptorProductSection {
  disruptor {
    ...DisruptorData
    __typename
  }
  __typename
}

fragment DisruptorData on Disruptor {
  __typename
  imageSrc {
    ...ImageAsset
    __typename
  }
  contrast
  background
  title
  description
  link
  openInNewTab
}

fragment ProductListings on ProductQueryResult {
  count
  offset
  total
  optimizelyExperiment {
    testId
    variantId
    __typename
  }
  results {
    ...Product_ProductItem
    __typename
  }
  facets {
    ...Facet_FacetSidebar
    __typename
  }
  sortOptions {
    ...Sort_SortOptions
    __typename
  }
  __typename
}

fragment Product_ProductItem on Product {
  __typename
  id
  productCode
  name
  slug
  primaryImage(size: THUMBNAIL)
  baseImgUrl: primaryImage
  overrideUrl
  ... on ReadOnlyProduct {
    readOnlyVariant {
      ...Variant_ReadOnlyProduct
      __typename
    }
    __typename
  }
  ... on SingleVariantProduct {
    variant {
      ...Variant_ListingProduct
      __typename
    }
    __typename
  }
  ... on MultiVariantProduct {
    priceRange {
      formattedPriceRange
      formattedListPriceRange
      __typename
    }
    variants {
      ...Variant_ListingProduct
      __typename
    }
    __typename
  }
}

fragment Variant_ListingProduct on ProductVariant {
  id
  sku
  salePercentage
  attributes {
    rating
    maxOrderQuantity
    availabilityStatus
    availabilityText
    vipAvailabilityStatus
    vipAvailabilityText
    canAddToBag
    canAddToWishlist
    vipCanAddToBag
    onSale
    isNew
    ...ProductAttributes_Flags
    __typename
  }
  ...ProductVariant_Pricing
  __typename
}

fragment ProductVariant_Pricing on ProductVariant {
  price {
    formattedAmount
    centAmount
    currencyCode
    formattedValue
    __typename
  }
  listPrice {
    formattedAmount
    centAmount
    __typename
  }
  attributes {
    onSale
    __typename
  }
  __typename
}

fragment ProductAttributes_Flags on ProductAttributes {
  featuredFlags {
    key
    label
    __typename
  }
  __typename
}

fragment Variant_ReadOnlyProduct on ReadOnlyVariant {
  id
  sku
  attributes {
    featuredFlags {
      key
      label
      __typename
    }
    __typename
  }
  __typename
}

fragment Facet_FacetSidebar on Facet {
  name
  key
  id
  labels {
    __typename
    displayMode
    name
    labelKey
    count
    ... on FacetValue {
      value
      __typename
    }
    ... on FacetRange {
      from
      to
      __typename
    }
  }
  __typename
}

fragment Sort_SortOptions on SortOptions {
  id
  key
  direction
  label
  __typename
}

fragment CardContentSection on CardContentSection {
  ...CardContent
  __typename
}

fragment CardContent on CardContentSection {
  moduleTitle
  showModuleTitle
  blocks {
    title
    isH1
    description
    textAlignment
    primaryLogoSrc {
      ...ImageAsset
      __typename
    }
    secondaryLogoSrc {
      ...ImageAsset
      __typename
    }
    logoPosition
    imageSrc {
      ...ImageAsset
      __typename
    }
    callToActionText
    callToActionLink
    altText
    contrast
    videoMedia {
      url
      id
      isLiveStream
      __typename
    }
    __typename
  }
  __typename
}

fragment CardCarouselSection on CardCarouselSection {
  ...CardCarouselContent
  __typename
}

fragment CardCarouselContent on CardCarouselSection {
  moduleTitle
  showModuleTitle
  blocks {
    title
    isH1
    description
    textAlignment
    primaryLogoSrc {
      ...ImageAsset
      __typename
    }
    secondaryLogoSrc {
      ...ImageAsset
      __typename
    }
    logoPosition
    imageSrc {
      ...ImageAsset
      __typename
    }
    callToActionText
    callToActionLink
    altText
    contrast
    videoMedia {
      url
      id
      isLiveStream
      __typename
    }
    __typename
  }
  __typename
}

fragment CopyContent on CopyContentSection {
  blocks {
    title
    body
    textAlignment
    titleColor
    imageSrc {
      ...ImageAsset
      __typename
    }
    __typename
  }
  __typename
}

fragment CopySectionData on CopySection {
  title
  showTitle
  body
  __typename
}

fragment QuickLinksData on QuickLinkSection {
  title
  quickLinks {
    title
    isH1
    link
    openInNewTab
    contrast
    imageSrc {
      ...ImageAsset
      __typename
    }
    __typename
  }
  __typename
}

fragment ContentBlockMixedData on ContentBlockMixed {
  moduleTitle
  showModuleTitle
  blocks {
    title
    isH1
    description
    backgroundColor
    blockTheme
    contentPosition
    logoURL
    logoPosition
    callToActionText
    callToActionLink
    altText
    backgroundImages {
      largeImage {
        small {
          ...ImageAsset
          __typename
        }
        large {
          ...ImageAsset
          __typename
        }
        __typename
      }
      smallImage {
        small {
          ...ImageAsset
          __typename
        }
        large {
          ...ImageAsset
          __typename
        }
        __typename
      }
      __typename
    }
    __typename
  }
  __typename
}

fragment UserGeneratedContentData on UserGeneratedContent {
  ugcBlock {
    title
    text
    ugcType
    ugcKey
    __typename
  }
  __typename
}

fragment HeroBannerData on HeroBanner {
  heroblocks {
    id
    title
    isH1
    tagline
    bannerTheme
    contentVerticalPosition
    contentHorizontalPosition
    contentHeight
    primaryLogoSrcNew {
      ...ImageAsset
      __typename
    }
    secondaryLogoSrcNew {
      ...ImageAsset
      __typename
    }
    videoMedia {
      url
      id
      isLiveStream
      __typename
    }
    logoPosition
    contentBackground
    callToActionText
    callToActionLink
    secondaryCallToActionText
    secondaryCallToActionLink
    secondaryOpenInNewTab
    backgroundImagesNew {
      small {
        ...ImageAsset
        __typename
      }
      medium {
        ...ImageAsset
        __typename
      }
      large {
        ...ImageAsset
        __typename
      }
      __typename
    }
    altText
    __typename
  }
  __typename
}

fragment GalleryData on Gallery {
  galleryblocks {
    id
    contentHeight
    primaryLogoSrcNew {
      ...ImageAsset
      __typename
    }
    videoMedia {
      url
      id
      isLiveStream
      __typename
    }
    backgroundImagesNew {
      small {
        ...ImageAsset
        __typename
      }
      medium {
        ...ImageAsset
        __typename
      }
      large {
        ...ImageAsset
        __typename
      }
      __typename
    }
    __typename
  }
  __typename
}

fragment MotionBannerData on MotionBanner {
  motionBannerBlocks {
    id
    title
    isH1
    tagline
    bannerTheme
    contentHorizontalPosition
    primaryLogoSrc {
      ...ImageAsset
      __typename
    }
    secondaryLogoSrc {
      ...ImageAsset
      __typename
    }
    animatedMedia
    videoMedia {
      url
      id
      isLiveStream
      __typename
    }
    logoPosition
    contentBackground
    callToActionText
    callToActionLink
    backgroundImages {
      small {
        ...ImageAsset
        __typename
      }
      medium {
        ...ImageAsset
        __typename
      }
      large {
        ...ImageAsset
        __typename
      }
      __typename
    }
    altText
    __typename
  }
  __typename
}

fragment MotionSidekickData on MotionSidekick {
  motionSidekickBlocks {
    id
    title
    isH1
    tagline
    bannerTheme
    contentHorizontalPosition
    primaryLogoSrc {
      ...ImageAsset
      __typename
    }
    secondaryLogoSrc {
      ...ImageAsset
      __typename
    }
    animatedMedia
    videoMedia {
      url
      id
      isLiveStream
      __typename
    }
    logoPosition
    contentBackground
    callToActionText
    callToActionLink
    backgroundImages {
      small {
        ...ImageAsset
        __typename
      }
      medium {
        ...ImageAsset
        __typename
      }
      large {
        ...ImageAsset
        __typename
      }
      __typename
    }
    altText
    __typename
  }
  __typename
}

fragment InPageNavData on InPageNav {
  inPageNavBlocks {
    id
    title
    isH1
    text
    contrast
    primaryLogoSrc
    secondaryLogoSrc
    animatedMedia
    videoMedia {
      url
      id
      __typename
    }
    contentBackground
    backgroundImages {
      small
      medium
      large
      __typename
    }
    callToActionText
    callToActionLink
    openInNewTab
    secondaryCallToActionText
    secondaryCallToActionLink
    secondaryOpenInNewTab
    __typename
  }
  __typename
}

fragment TableData on TableSection {
  rows {
    isHeadingRow
    cells
    __typename
  }
  __typename
}

fragment RecommendationSectionData on RecommendationSection {
  __typename
  title
  showTitle
  recommendationType
}

fragment SidekickBannerData on SidekickBanner {
  __typename
  id
  sidekickBlocks {
    title
    isH1
    text
    textAlignment
    contrast
    backgroundColor
    logoSrc {
      ...ImageAsset
      __typename
    }
    secondaryLogoSrc {
      ...ImageAsset
      __typename
    }
    logoPosition
    ctaTextPrimary: ctaText
    ctaLinkPrimary: ctaLink
    ctaTextSecondary
    ctaLinkSecondary
    contentHeight
    bgImages {
      large
      __typename
    }
    videoMedia {
      url
      id
      isLiveStream
      __typename
    }
    altText
    __typename
  }
}

fragment ProductCarousel_UniqueFields on ProductCarouselSection {
  __typename
  productCarouselTitle: title
  showTitle
  showAddToBag
  seeAllLink
}

fragment CustomProductCarousel_UniqueFields on CustomProductCarouselSection {
  __typename
  productCarouselTitle: title
  showTitle
  showAddToBag
  seeAllLink
  backgroundColor
}

fragment CustomProductCarousel_ItemFields on CustomProductCarouselItem {
  product {
    ...Product_ProductItem
    __typename
  }
  imageOverride {
    ...ImageAsset
    __typename
  }
  imageBackgroundColor
  contentBackgroundColor
  ctaButtonColor
  __typename
}

fragment TextBlockData on TextBlock {
  textBlocks {
    title
    isH1
    text
    textAlignment
    contrast
    backgroundColor
    callToActionLink
    callToActionText
    openInNewTab
    secondaryCallToActionLink
    secondaryCallToActionText
    secondaryOpenInNewTab
    __typename
  }
  __typename
}

fragment TextBlockSEOData on TextBlockSEO {
  textBlocks {
    title
    text
    __typename
  }
  __typename
}

fragment Countdown on CountdownBannerChild {
  title
  isH1
  text
  textPosition
  textAlignment
  contrast
  backgroundColor
  callToActionLink
  callToActionText
  openInNewTab
  countdownDate
  __typename
}

fragment CountdownBannerData on CountdownBanner {
  countdownBannerBlocks {
    ...Countdown
    __typename
  }
  __typename
}

fragment CountdownSection on CountdownProductSection {
  countdown {
    ...Countdown
    __typename
  }
  __typename
}

fragment CrowdTwistWidgetSection on CrowdTwistWidgetSection {
  __typename
  id
  heading
  activityId
  rewardId
}

fragment CodedSection on CodedSection {
  __typename
  id
  componentName
  properties {
    key
    value
    __typename
  }
  text {
    key
    value
    __typename
  }
  media {
    key
    values {
      id
      contentType
      fileSize
      filename
      url
      title
      __typename
    }
    __typename
  }
}

fragment GridSectionData on GridSection {
  items {
    id
    image
    videoMedia {
      id
      url
      isLiveStream
      __typename
    }
    href
    text
    textContrast
    __typename
  }
  __typename
}

fragment AudioSectionData on AudioSection {
  tracks {
    trackArt {
      ...ImageAsset
      __typename
    }
    src
    title
    description
    __typename
  }
  backgroundColor
  textContrast
  backgroundImage {
    mobile {
      ...ImageAsset
      __typename
    }
    desktop {
      ...ImageAsset
      __typename
    }
    __typename
  }
  seriesTitle
  seriesThumbnail {
    ...ImageAsset
    __typename
  }
  __typename
}

fragment Breadcrumbs on Content {
  breadcrumbs {
    __typename
    label
    url
    analyticsTitle
  }
  __typename
}

fragment StickyCTAData on StickyCTASection {
  item {
    backgroundColor
    ctaBackgroundImage
    ctaPosition
    href
    text
    textAlign
    textContrast
    __typename
  }
  __typename
}

fragment MotionSidekick1x1Data on MotionSidekick1x1 {
  motionSidekickBlocks {
    id
    title
    description
    textContrast
    contentHorizontalPosition
    primaryLogoSrc {
      ...ImageAsset
      __typename
    }
    secondaryLogoSrc {
      ...ImageAsset
      __typename
    }
    inlineVideo {
      id
      url
      isLiveStream
      __typename
    }
    fullVideo {
      id
      url
      isLiveStream
      __typename
    }
    logoHorizontalPosition
    backgroundColor
    primaryCallToActionText
    primaryCallToActionLink
    secondaryCallToActionText
    secondaryCallToActionLink
    __typename
  }
  __typename
}

fragment ImageTransitionSliderData on ImageTransitionSlider {
  imageTransitionSliderBlocks {
    id
    title
    description
    backgroundColor
    contrast
    ctas {
      link
      text
      __typename
    }
    contentHorizontalPosition
    firstImage {
      ...ImageAsset
      __typename
    }
    secondImage {
      ...ImageAsset
      __typename
    }
    __typename
  }
  __typename
}

fragment PollsSectionData on PollsSection {
  id
  question
  backgroundColor
  answerFillColor
  answerBorderColor
  answers {
    answer
    id
    __typename
  }
  textContrast
  image {
    ...ImageAsset
    __typename
  }
  imageAlignment
  pollResults {
    answers {
      answerId
      count
      __typename
    }
    totalVotes
    __typename
  }
  __typename
}

fragment ArtNavigationData on ArtNavigation {
  artNavigationBlocks {
    id
    title
    callToActionLink
    backgroundImage {
      ...ImageAsset
      __typename
    }
    logoImage {
      ...ImageAsset
      __typename
    }
    textImage {
      ...ImageAsset
      __typename
    }
    __typename
  }
  __typename
}
"""
